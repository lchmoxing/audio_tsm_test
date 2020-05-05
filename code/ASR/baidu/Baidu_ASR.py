# coding=utf-8

import os
import sys
import json
import time
import ast
import numpy as np
import pandas as pd
import csv
from jiwer import wer

IS_PY3 = sys.version_info.major == 3
path =os.path.abspath('..')
path =os.path.dirname(path)
path1 =os.path.dirname(path)
print(path1)

if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request

    from urllib.error import HTTPError
    from urllib.parse import urlencode

    timer = time.perf_counter
else:
    import urllib.request
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.request import HTTPError
    from urllib.parse import urlencode

    if sys.platform == "win32":
        timer = time.clock
    else:
        # On most other platforms the best timer is time.time()
        timer = time.time

# API_KEY = 'gvdGH9Suir9sQ6ChtPVvWQhN'   
# SECRET_KEY = 'I053HzhvDRvDmqpx4mEBPuqG6UesSRZv'
API_KEY = 'T5sA7FUN2803vZfVURRG8Fz0'   
SECRET_KEY = 'KHG7i6cS8Dksy2oSIDSGl0k1rHbC1L8L'

# # 需要识别的文件
AUDIO_FILE = path1 + '/dataset/speech_origin/without_wake_words/16k/' + str(1) +'.wav'  # 只支持 pcm/wav/amr 格式，极速版额外支持m4a 格式
# TEXT_FILE = 'C:/Users/73936/Desktop/baidutest.txt'
# 文件格式
FORMAT = AUDIO_FILE[-3:]  # 文件后缀只支持 pcm/wav/amr 格式，极速版额外支持m4a 格式

CUID = '123456PYTHON'
# 采样率
RATE = 16000;  # 固定值

# 普通版


DEV_PID = 1737;  # 1737 表示识别英文，使用输入法模型。根据文档填写PID，选择语言及识别模型
ASR_URL = 'http://vop.baidu.com/server_api'
SCOPE = 'audio_voice_assistant_get'  # 有此scope表示有asr能力，没有请在网页里勾选，非常旧的应用可能没有


class DemoError(Exception):
    pass


"""  TOKEN start """

TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'


def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req)
        result_str = f.read()
    except HTTPError as err:
        # print('token http response http code : ' + str(err.code))
        result_str = err.read()
    if (IS_PY3):
        result_str = result_str.decode()

    # print(result_str)
    result = json.loads(result_str)
    # print(result)
    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if SCOPE and (not SCOPE in result['scope'].split(' ')):  # SCOPE = False 忽略检查
            raise DemoError('scope is not correct')
        # print('SUCCESS WITH TOKEN: %s ; EXPIRES IN SECONDS: %s' % (result['access_token'], result['expires_in']))
        return result['access_token']
    else:
        raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')


"""  TOKEN end """

def write_csv_file(path, head, data):
    try:
        with open(path, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, dialect='excel')
            if head is not None:
                writer.writerow(head)
            for row in data:
                writer.writerow(row)
            print("Write a CSV file to path %s Successful." % path)
        csv_file.close()
    except Exception as e:
        print("Write an CSV file to path: %s, Case: %s" % (path, e))

path = os.getcwd()
path = os.path.join(path+r"\baidu.csv")
origin_result = []
phasevoctor_result = []
ola_result = []
wsola_result = []
def baidu_asr(AUDIO_FILE, TEXT_FILE):
    token = fetch_token()

    """
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    opener = urllib2.build_opener(httpHandler)
    urllib2.install_opener(opener)
    """

    speech_data = []
    with open(AUDIO_FILE, 'rb') as speech_file:
        speech_data = speech_file.read()
    length = len(speech_data)
    if length == 0:
        raise DemoError('file %s length read 0 bytes' % AUDIO_FILE)

    params = {'cuid': CUID, 'token': token, 'dev_pid': DEV_PID}
    #测试自训练平台需要打开以下信息
    #params = {'cuid': CUID, 'token': token, 'dev_pid': DEV_PID, 'lm_id' : LM_ID}
    params_query = urlencode(params)

    headers = {
        'Content-Type': 'audio/' + FORMAT + '; rate=' + str(RATE),
        'Content-Length': length
    }

    url = ASR_URL + "?" + params_query
    # print("url is", url);
    # print("header is", headers)
    # print post_data
    req = Request(ASR_URL + "?" + params_query, speech_data, headers)
    try:
        begin = timer()
        f = urlopen(req)
        result_str = f.read()
        # print("Request time cost %f" % (timer() - begin))
    except  HTTPError as err:
        # print('asr http response http code : ' + str(err.code))
        result_str = err.read()

    if (IS_PY3):
        # print(type(result_str))
        result_str = str(result_str, 'utf-8')
        # result_str = ast.literal_eval(result_str)
        result_str = json.loads(result_str, strict=False)
        print(result_str)
        if (result_str["err_msg"] == "success."):
            result_text = str(result_str["result"])
            result_text = result_text.replace('[','').replace(']','').replace('\'','')
            print(result_text)
            # with open(TEXT_FILE, "a") as file_object:
            #      file_object.write(result_text + '\n')
        else:
            print("error")
            result_text = 'error'
        if (AUDIO_FILE == audio_origin):
            origin_result.append(result_text.lower())
        elif (AUDIO_FILE == audio_phasevoctor):
            phasevoctor_result.append(result_text.lower())
        elif (AUDIO_FILE == audio_ola):
            ola_result.append(result_text.lower())
        elif (AUDIO_FILE == audio_wsola):
            wsola_result.append(result_text.lower())
            # with open(TEXT_FILE, "a") as file_object:
            #      file_object.write("error!" + str(result_str["err_no"]) + '\n')

num = 0
for i in np.arange(0.25, 3.0, 0.25):
    for num in range(0, 10):
        num +=1
        ### voice with wake words
        # audio_origin = 'C:/Users/73936/Desktop/voice_speech/dataset/' + str(num) +'.wav'
        # baidu_asr_origin = 'C:/github_code/audio_tsm_test/test_result/baidu/baidu_origin.txt'
        ### voice without wake words
        # print(os.path.abspath(os.path.dirname(sys.argv[0])))
        audio_origin = path1 + '/dataset/speech_origin/without_wake_words/16k/' + str(num) +'.wav'
        baidu_asr_origin = path1 + '/test_result/baidu/16k/without_wake_words/baidu_origin.txt'
        # ### voice with wake words
        # audio_phasevoctor = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/phasevoctor' + str(i) + '_' + str(num) +'.wav'
        # audio_ola = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/ola' + str(i) + '_' + str(num) +'.wav'
        # audio_wsola = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/wsola' + str(i) + '_' + str(num) +'.wav'

        # baidu_asr_phasevoctor = 'C:/github_code/audio_tsm_test/test_result/baidu/baidu_asr_phasevoctor' + str(i) + '.txt'
        # baidu_asr_ola = 'C:/github_code/audio_tsm_test/test_result/baidu/baidu_asr_ola' + str(i) + '.txt'
        # baidu_asr_wsola = 'C:/github_code/audio_tsm_test/test_result/baidu/baidu_asr_wsola' + str(i) + '.txt'       
        
        ### voice without wake words
        audio_phasevoctor = path1 + '/dataset/16k/without_wake_words/phasevoctor' + str(i) + '_' + str(num) +'.wav'
        audio_ola = path1 + '/dataset/16k/without_wake_words/ola' + str(i) + '_' + str(num) +'.wav'
        audio_wsola = path1 + '/dataset/16k/without_wake_words/wsola' + str(i) + '_' + str(num) +'.wav'

        baidu_asr_phasevoctor = path1 + '/test_result/baidu/16k/without_wake_words/baidu_asr_phasevoctor' + str(i) + '.txt'
        baidu_asr_ola = path1 + '/test_result/baidu/16k/without_wake_words/baidu_asr_ola' + str(i) + '.txt'
        baidu_asr_wsola = path1 + '/test_result/baidu/16k/without_wake_words/baidu_asr_wsola' + str(i) + '.txt'  
        if(i == 0.25):
            baidu_asr(audio_origin, baidu_asr_origin)
        baidu_asr(audio_phasevoctor, baidu_asr_phasevoctor)
        baidu_asr(audio_ola, baidu_asr_ola)
        baidu_asr(audio_wsola, baidu_asr_wsola)
    if(i==0.25):
        write_csv_file(path,["origin","phasevoctor"+str(i),"ola"+str(i),"wsola"+str(i)],np.array([ola_result,phasevoctor_result,ola_result,wsola_result]).T)
        df = pd.read_csv(path,error_bad_lines=False)
        print("write successfully!" + str(i))
    else:
        df["phasevoctor"+str(i)] = phasevoctor_result
        df["ola"+str(i)] = ola_result
        df["wsola"+str(i)] = wsola_result
        df.to_csv(path, mode ='w', index=False)
        print("write successfully!" + str(i))
    origin_result.clear()
    phasevoctor_result.clear()
    ola_result.clear()
    wsola_result.clear()
print("successfully")