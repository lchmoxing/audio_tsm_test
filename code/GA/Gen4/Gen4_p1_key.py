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

import os
from pydub import AudioSegment
import wave
import time
import numpy as np
import shutil
import random
import tensorflow as tf
from audiotsm import phasevocoder, ola, wsola
from audiotsm.io.wav import WavReader, WavWriter
import Levenshtein
from jiwer import wer
from itertools import combinations
from scipy.special import perm, comb

global Results


def convert_samplerate(audio_path, desired_sample_rate):
    sox_cmd = 'sox {} --type raw --bits 16 --channels 1 --rate {} --encoding signed-integer --endian little --compression 0.0 --no-dither - '.format(
        quote(audio_path), desired_sample_rate)
    try:
        output = subprocess.check_output(shlex.split(sox_cmd), stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        raise RuntimeError('SoX returned non-zero status: {}'.format(e.stderr))
    except OSError as e:
        raise OSError(e.errno,
                      'SoX not found, use {}hz files or install it: {}'.format(desired_sample_rate, e.strerror))

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
        print(
            'Warning: original sample rate ({}) is different than {}hz. Resampling might produce erratic speech recognition.'.format(
                fs_orig, desired_sample_rate), file=sys.stderr)
        fs_new, audio = convert_samplerate(audio_input, desired_sample_rate)
    else:
        audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)

    audio_length = fin.getnframes() * (1 / fs_orig)
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
    return (Results)


def audio_split(input_file_path, split_time):
    wav_time = AudioSegment.from_file(input_file_path).duration_seconds
    wav_time = int(wav_time * 1000)
    # print(wav_time)
    start_time = 0
    end_time = split_time
    sound = AudioSegment.from_wav(input_file_path)
    (filepath, tempfilename) = os.path.split(input_file_path)
    for i in range(1, (wav_time // split_time + 2)):
        output_file_path = filepath + '\speech_split' + '\\' + tempfilename[:-4] + '\\' + str(i) + '.wav'
        word = sound[start_time:end_time]
        word.export(output_file_path, format='wav')
        start_time += split_time
        end_time += split_time


def audio_join(input_dir, output_dir):
    join_sound_lists = AudioSegment.empty()
    for i in range(len(os.listdir(input_dir))):
        filename = input_dir + '/' + str(i + 1) + '.wav'
        join_sound_lists += AudioSegment.from_wav(filename)
    join_sound_lists.export(output_dir, format="wav")
    print("audio_join successfully")


def audio_tsm(ca_type, i, input_filename, output_filename):
    with WavReader(input_filename) as reader:
        with WavWriter(output_filename, reader.channels, reader.samplerate) as writer_tsm:
            if (ca_type == phasevocoder):
                tsm = phasevocoder(reader.channels, speed=i)
            if (ca_type == ola):
                tsm = ola(reader.channels, speed=i)
            if (ca_type == wsola):
                tsm = wsola(reader.channels, speed=i)
            tsm.run(reader, writer_tsm)
    # print("audio_tsm successfully")


def Levenshtein_similarity(origin, target):
    ls_result = Levenshtein.ratio(origin, target)
    return ls_result

def softmax(x):
    x_exp = np.exp(x)
    #如果是列向量，则axis=0
    x_sum = np.sum(x_exp, axis = 0, keepdims = True)
    s = x_exp / x_sum
    return s

def selection_father(fitness_score_raw):
    #计算累加倍率#
    fitness_score_sum = 0
    fitness_score_distri = np.zeros(len(fitness_score_raw))
    fitness_score_cum =  np.zeros(len(fitness_score_raw))
    parent_tmp = 0
    for i in range(len(fitness_score_raw)):
        fitness_score_sum = fitness_score_sum + fitness_score_raw[i]
    for j in range(len(fitness_score_raw)):
        fitness_score_distri[j] = fitness_score_raw[j] / fitness_score_sum
        if j == 0:
            fitness_score_cum[j] = fitness_score_distri[j]
        else:
            fitness_score_cum[j] = fitness_score_cum[j-1] + fitness_score_distri[j]
    # print(fitness_score_distri)
    # print(fitness_score_cum)
    ##轮盘赌
    for n in range(len(fitness_score_cum)):
        random_tmp = np.random.random(1)
        # print(random_tmp)
        if fitness_score_cum[n] > random_tmp:
            parent_tmp = n
            break
    return  parent_tmp

def crossover(pp1,pp2, perturb_speed,fitness_score):
    sp1 = fitness_score[pp1]
    sp2 = fitness_score[pp2]
    if sp1 == 0 and sp2 == 0:
        select_p = 0.5
    else:
        select_p = sp1 /(sp1+sp2)
 #   print(select_p)
    perturb_tmp = np.zeros(perturb_speed.shape[1])
    # print(sp1)
    # print(sp2)
    # print(select_p)
    for i in range(perturb_speed.shape[1]):
        random_tmp = np.random.random(1)
  #      print(random_tmp)qsgn
        if select_p > random_tmp:
            perturb_tmp[i] = perturb_speed[pp1][i]
        else:
            perturb_tmp[i] = perturb_speed[pp2][i]
   #     print(perturb_tmp)
    return perturb_tmp

def mutation(pop_num, perturb_speed_tmp, mutation_rate, mutation_step,mutation_range):
    for i in range(len(perturb_speed_tmp[pop_num])):
        random_tmp = np.random.random(1)
        # print(random_tmp)
        if mutation_rate > random_tmp:
            # print(perturb_speed_tmp[pop_num][i])
            perturb_speed_tmp[pop_num][i] = perturb_speed_tmp[pop_num][i] + \
                                            int(mutation_step * random.randrange(-mutation_range, mutation_range, 1))
            # print(perturb_speed_tmp[pop_num][i])
            if perturb_speed_tmp[pop_num][i] < 5:
                perturb_speed_tmp[pop_num][i] = 5
            elif perturb_speed_tmp[pop_num][i] > 20:
                perturb_speed_tmp[pop_num][i] = 20
    return  perturb_speed_tmp[pop_num]




if __name__ == '__main__':
    pop_max = 100
    gen_max = 500
    k = 0.8
    target = 'door'
    mutation_rate = 0.1
    mutation_step = 0.3
    speed_max = 20
    speed_min = 5
    mutation_range = speed_max - speed_min

    # Create initial generation#
    gen = 1
    path1 = r"/home/usslab/qinhong/deepspeech/audio/speech_split/picture_1_50ms"
    split_frame_num = len(os.listdir(path1))

    perturb_speed = np.random.randint(speed_min, speed_max, (pop_max, split_frame_num))
    perturb_speed_tmp = np.zeros((pop_max, split_frame_num))
    perturb_speed_mutation_tmp = np.zeros((pop_max, split_frame_num))
    hypothesis = []
    fitness_score = []
    filename = r"/home/usslab/qinhong/deepspeech/audio/speech_split/output_door_g4/result_door_g4.txt"
    file = open(filename, mode='w+', encoding='utf-8')
    file.write('GA start!'+'\n')
    file.close()

    for i in range(pop_max):
        for j in range(split_frame_num):
            tsm_in_path = path1 + '/' + "1_{}.wav".format(str(j+1))
            tsm_out_path = r"/home/usslab/qinhong/deepspeech/audio/speech_split/tsm_door_g4/" + str(j + 1) + '.wav'
            v = perturb_speed[i][j] / 10
            audio_tsm(ola, v, tsm_in_path, tsm_out_path)
        join_input_path = r"/home/usslab/qinhong/deepspeech/audio/speech_split/tsm_door_g4"
        join_output_path = r"/home/usslab/qinhong/deepspeech/audio/speech_split/output_door_g4/" + str(gen) + '_' + str(
            i + 1) + '.wav'
        audio_join(join_input_path, join_output_path)
        result_tmp = asr_deepspeech(join_output_path)

        if result_tmp != '':
            with open(filename, 'a') as file_object:
                file_object.write(str(gen) + '_' + str(i+1) + ':' + result_tmp + '\n')
                file_object.write('speed_sequence' + ':')
                for j in range(split_frame_num):
                    file_object.write(str(perturb_speed[i][j]) + '_')
                file_object.write('\n')

        hypothesis.append(result_tmp)
##计算fitness
        fitness_score.append(Levenshtein_similarity(result_tmp, target))
##找到精英
    elite_index = fitness_score.index(max(fitness_score))
    elite = hypothesis[elite_index]
    if max(fitness_score) == 1:
        print("Find successful attack")
    print(hypothesis)
    # print(perturb_speed)
    print(fitness_score)
    print(elite_index)
    print(elite)
## 精英继承到下一代
    perturb_speed_tmp[0] = perturb_speed[elite_index]

#crossover孩子交叉#
    crossover_size = pop_max - 1
    for i in range(crossover_size):
        pp1_index = selection_father(fitness_score)
        pp2_index = selection_father(fitness_score)
        perturb_speed_tmp[i + 1] = crossover(pp1_index, pp2_index, perturb_speed, fitness_score)
        # print(pp1_index)
        # print(pp2_index)
        # print(perturb_speed[pp1_index])
        # print(perturb_speed[pp2_index])
    print(perturb_speed_tmp)

    for j in range(pop_max):
        perturb_speed_mutation_tmp[j] = mutation(j, perturb_speed_tmp, mutation_rate, mutation_step,mutation_range)
        # print(perturb_speed_mutation_tmp[j])

    print(perturb_speed_mutation_tmp)

    gen = gen + 1
    # 开始迭代#
    while gen < gen_max:
        perturb_speed = perturb_speed_mutation_tmp
        perturb_speed_tmp = np.zeros((pop_max, split_frame_num))
        perturb_speed_mutation_tmp = np.zeros((pop_max, split_frame_num))
        hypothesis = []
        fitness_score = []
        for i in range(pop_max):
            for j in range(split_frame_num):
                tsm_in_path = path1 + '/' + "1_{}.wav".format(str(j+1))
                tsm_out_path = r"/home/usslab/qinhong/deepspeech/audio/speech_split/tsm_door_g4/" + str(j + 1) + '.wav'
                v = perturb_speed[i][j] / 10
                audio_tsm(ola, v, tsm_in_path, tsm_out_path)
            join_input_path = r"/home/usslab/qinhong/deepspeech/audio/speech_split/tsm_door_g4"
            join_output_path = r"/home/usslab/qinhong/deepspeech/audio/speech_split/output_door_g4/" + str(gen) + '_' + str(
                i + 1) + '.wav'
            audio_join(join_input_path, join_output_path)
            result_tmp = asr_deepspeech(join_output_path)
            if result_tmp != '':
                with open(filename, 'a') as file_object:
                    file_object.write(str(gen) + '_' + str(i+1) + ':' + result_tmp + '\n')
                    file_object.write('speed_sequence' + ':')
                    for j in range(split_frame_num):
                        file_object.write(str(perturb_speed[i][j]) + '_')
                    file_object.write('\n')
            hypothesis.append(result_tmp)
        ##计算fitness
            fitness_score.append(Levenshtein_similarity(result_tmp, target))
        ##找到精英
        elite_index = fitness_score.index(max(fitness_score))
        elite = hypothesis[elite_index]
        if max(fitness_score) == 1:
            print("Find successful attack")
            break
        print(hypothesis)
        # print(perturb_speed)
        print(fitness_score)
        print(elite_index)
        print(elite)
        ## 精英继承到下一代
        perturb_speed_tmp[0] = perturb_speed[elite_index]

        # crossover孩子交叉#
        # crossover_size = pop_max - 1
        for i in range(crossover_size):
            pp1_index = selection_father(fitness_score)
            pp2_index = selection_father(fitness_score)
            perturb_speed_tmp[i + 1] = crossover(pp1_index, pp2_index, perturb_speed, fitness_score)
            # print(pp1_index)
            # print(pp2_index)
            # print(perturb_speed[pp1_index])
            # print(perturb_speed[pp2_index])
        print(perturb_speed_tmp)

        for j in range(pop_max):
            perturb_speed_mutation_tmp[j] = mutation(j, perturb_speed_tmp, mutation_rate, mutation_step, mutation_range)
            # print(perturb_speed_mutation_tmp[j])

        print(perturb_speed_mutation_tmp)
        gen = gen + 1

##


# fitness需要修改#
# def compute_fitness(hypothesis, target):
#     target_score = Levenshtein_similarity(hypothesis, target)
#     return target_score

