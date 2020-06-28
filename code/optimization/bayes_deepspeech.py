##deepspeech
from __future__ import absolute_import, division, print_function

import argparse
import shlex
import subprocess
import sys
import json
# import pandas as pd

from deepspeech import Model, version
from timeit import default_timer as timer


try:
    from shhlex import quote
    
except ImportError:
    from pipes import quote


from bayes_opt import BayesianOptimization
import os
from pydub import AudioSegment
import wave
import numpy as np
import shutil
import random
from audiotsm import phasevocoder, ola, wsola
from audiotsm.io.wav import WavReader, WavWriter
from jiwer import wer
from itertools import combinations
from scipy.special import perm, comb



global Results
def convert_samplerate(audio_path, desired_sample_rate):
    sox_cmd = 'sox {} --type raw --bits 16 --channels 1 --rate {} --encoding signed-integer --endian little --compression 0.0 --no-dither - '.format(quote(audio_path), desired_sample_rate)
    try:
        output = subprocess.check_output(shlex.split(sox_cmd), stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        raise RuntimeError('SoX returned non-zero status: {}'.format(e.stderr))
    except OSError as e:
        raise OSError(e.errno, 'SoX not found, use {}hz files or install it: {}'.format(desired_sample_rate, e.strerror))

    return desired_sample_rate, np.frombuffer(output, np.int16)


def metadata_to_string(metadata):
    return ''.join(token.text for token in metadata.tokens)


def words_from_candidate_transcript(metadata):
    word = ""
    word_list = []
    word_start_time = 0
    # Loop through each character
    for i, token in enumerate(metadata.tokens):
        # Append character to word if it's not a space
        if token.text != " ":
            if len(word) == 0:
                # Log the start time of the new word
                word_start_time = token.start_time

            word = word + token.text
        # Word boundary is either a space or the last character in the array
        if token.text == " " or i == len(metadata.tokens) - 1:
            word_duration = token.start_time - word_start_time

            if word_duration < 0:
                word_duration = 0

            each_word = dict()
            each_word["word"] = word
            each_word["start_time "] = round(word_start_time, 4)
            each_word["duration"] = round(word_duration, 4)

            word_list.append(each_word)
            # Reset
            word = ""
            word_start_time = 0

    return word_list


def metadata_json_output(metadata):
    json_result = dict()
    json_result["transcripts"] = [{
        "confidence": transcript.confidence,
        "words": words_from_candidate_transcript(transcript),
    } for transcript in metadata.transcripts]
    return json.dumps(json_result, indent=2)



class VersionAction(argparse.Action):
    def __init__(self, *args, **kwargs):
        super(VersionAction, self).__init__(nargs=0, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print('DeepSpeech ', version())
        exit(0)


def asr_deepspeech(audio_input):
    parser = argparse.ArgumentParser(description='Running DeepSpeech inference.')
    parser.add_argument('--model', required=True,
                        help='Path to the model (protocol buffer binary file)')
    parser.add_argument('--scorer', required=False,
                        help='Path to the external scorer file')
    # parser.add_argument('--audio', required=True,
    #                     help='Path to the audio file to run (WAV format)')
    parser.add_argument('--beam_width', type=int,
                        help='Beam width for the CTC decoder')
    parser.add_argument('--lm_alpha', type=float,
                        help='Language model weight (lm_alpha). If not specified, use default from the scorer package.')
    parser.add_argument('--lm_beta', type=float,
                        help='Word insertion bonus (lm_beta). If not specified, use default from the scorer package.')
    parser.add_argument('--version', action=VersionAction,
                        help='Print version and exits')
    parser.add_argument('--extended', required=False, action='store_true',
                        help='Output string from extended metadata')
    parser.add_argument('--json', required=False, action='store_true',
                        help='Output json from metadata with timestamp of each word')
    parser.add_argument('--candidate_transcripts', type=int, default=3,
                        help='Number of candidate transcripts to include in JSON output')
    args = parser.parse_args()

    print('Loading model from file {}'.format(args.model), file=sys.stderr)
    model_load_start = timer()
    # sphinx-doc: python_ref_model_start
    ds = Model(args.model)
    # sphinx-doc: python_ref_model_stop
    model_load_end = timer() - model_load_start
    print('Loaded model in {:.3}s.'.format(model_load_end), file=sys.stderr)

    if args.beam_width:
        ds.setBeamWidth(args.beam_width)

    desired_sample_rate = ds.sampleRate()

    if args.scorer:
        print('Loading scorer from files {}'.format(args.scorer), file=sys.stderr)
        scorer_load_start = timer()
        ds.enableExternalScorer(args.scorer)
        scorer_load_end = timer() - scorer_load_start
        print('Loaded scorer in {:.3}s.'.format(scorer_load_end), file=sys.stderr)

        if args.lm_alpha and args.lm_beta:
            ds.setScorerAlphaBeta(args.lm_alpha, args.lm_beta)

    fin = wave.open(audio_input, 'rb')
    fs_orig = fin.getframerate()
    if fs_orig != desired_sample_rate:
        print('Warning: original sample rate ({}) is different than {}hz. Resampling might produce erratic speech recognition.'.format(fs_orig, desired_sample_rate), file=sys.stderr)
        fs_new, audio = convert_samplerate(audio_input, desired_sample_rate)
    else:
        audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)

    audio_length = fin.getnframes() * (1/fs_orig)
    fin.close()

    print('Running inference.', file=sys.stderr)
    inference_start = timer()
    # sphinx-doc: python_ref_inference_start
    if args.extended:
        print(metadata_to_string(ds.sttWithMetadata(audio, 1).transcripts[0]))
    elif args.json:
        print(metadata_json_output(ds.sttWithMetadata(audio, args.candidate_transcripts)))
    else:
        print(ds.stt(audio))
        Results = ds.stt(audio)
    inference_end = timer() - inference_start
    print('Inference took %0.3fs for %0.3fs audio file.' % (inference_end, audio_length), file=sys.stderr)
    return(Results)

def audio_split(input_file_path, split_time):
    wav_time =AudioSegment.from_file(input_file_path).duration_seconds
    wav_time = int(wav_time * 1000)
    # print(wav_time)
    start_time = 0
    end_time = split_time
    sound = AudioSegment.from_wav(input_file_path)
    (filepath,tempfilename) = os.path.split(input_file_path)
    for i in range(1,(wav_time//split_time+2)):
        output_file_path = filepath + '\speech_split' +'\\' + tempfilename[:-4] + '\\' + str(i) + '.wav'
        word = sound[start_time:end_time]
        word.export(output_file_path,format='wav')
        start_time += split_time
        end_time += split_time  

def audio_join(input_dir, output_dir):
    join_sound_lists = AudioSegment.empty()
    for i in range(len(os.listdir(input_dir))):
        filename = input_dir + '/'  +str(i + 1) + '.wav'
        join_sound_lists += AudioSegment.from_wav(filename)
    join_sound_lists.export(output_dir, format="wav")
    print("audio_join successfully")

def audio_tsm(ca_type,i,input_filename,output_filename):
    with WavReader(input_filename) as reader:
        with WavWriter(output_filename, reader.channels, reader.samplerate) as writer_tsm:
            if (ca_type == phasevocoder):
                tsm = phasevocoder(reader.channels, speed=i)
            if (ca_type == ola):
                tsm = ola(reader.channels, speed=i)
            if (ca_type == wsola):
                tsm = wsola(reader.channels, speed=i)
            tsm.run(reader, writer_tsm)
    #print("audio_tsm successfully")

def black_box_function(slot_num ,tsm_speed):
    """Function with unknown internals we wish to maximize.

    This is just serving as an example, for all intents and
    purposes think of the internals of this function, i.e.: the process
    which generates its output values, as unknown.
    """
    slot_num = int(slot_num)
    tsm_speed = int(tsm_speed)
    path1 = r"/home/usslab/qinhong/deepspeech/audio/speech_split/picture"
    # path1 =r"/home/usslab/qinhong/deepspeech/speech_split_tsm_join/split_origin/1"
    # join_input_path = r"/home/usslab/qinhong/deepspeech/speech_split_tsm_join/split_test/1"
    # shutil.copytree(path1, join_input_path)
    permutations = [c for c in  combinations(range(1,len(os.listdir(path1))+1), slot_num)]#排列组合的所有可能性
    combs = comb(len(os.listdir(path1)), slot_num)#排列组合的总数目
    for m in range(int(combs)):
        # shutil.copytree(path1, join_input_path)
        for n in range(slot_num):
            j = permutations[m][n]
            tsm_in_path = path1 +'/' + str(j) + '.wav'
            tsm_out_path = r"/home/usslab/qinhong/deepspeech/audio/speech_split/tsm/" + str(j) + '.wav'
            v = tsm_speed/10
            audio_tsm(ola, v, tsm_in_path, tsm_out_path)
        join_input_path = r"/home/usslab/qinhong/deepspeech/audio/speech_split/tsm"
        join_output_path = r"/home/usslab/qinhong/deepspeech/audio/speech_split/output/"  + str(slot_num) + '_' + str(tsm_speed) + '_'+str(m+1) + '.wav'
        audio_join(join_input_path,join_output_path)
        hypothesis = asr_deepspeech(join_output_path)
        asr_wer = wer("turn", hypothesis)
        # shutil.rmtree(join_input_path)
        # if not os.path.isdir(join_input_path):
        #     os.makedirs(join_input_path)
    return (1-asr_wer)
# Bounded region of parameter space
pbounds = {'slot_num': (1, 8), 'tsm_speed': (5, 15)}

optimizer = BayesianOptimization( 
    f=black_box_function,
    pbounds=pbounds,
    random_state=1,
)


optimizer.maximize(
    init_points=10,
    n_iter=2000,
)