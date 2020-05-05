# -*- coding:utf-8 -*-
#
#   author: qinhong
#
#  本demo测试时运行的环境为：Windows + Python3.7
#  查看代码直接看main部分
#  本demo测试成功运行时所安装的第三方库及其版本如下，您可自行逐一或者复制到一个新的txt文件利用pip一次性安装：
#   cffi==1.12.3
#   gevent==1.4.0
#   greenlet==0.4.15
#   pycparser==2.19
#   six==1.12.0
#   websocket==0.2.1
#   websocket-client==0.56.0
#
#  语音听写流式 WebAPI 接口调用示例 接口文档（必看）：https://doc.xfyun.cn/rest_api/语音听写（流式版）.html
#  webapi 听写服务参考帖子（必看）：http://bbs.xfyun.cn/forum.php?mod=viewthread&tid=38947&extra=
#  语音听写流式WebAPI 服务，热词使用方式：登陆开放平台https://www.xfyun.cn/后，找到控制台--我的应用---语音听写（流式）---服务管理--个性化热词，
#  设置热词
#  注意：热词只能在识别的时候会增加热词的识别权重，需要注意的是增加相应词条的识别率，但并不是绝对的，具体效果以您测试为准。
#  语音听写流式WebAPI 服务，方言试用方法：登陆开放平台https://www.xfyun.cn/后，找到控制台--我的应用---语音听写（流式）---服务管理--识别语种列表
#  可添加语种或方言，添加后会显示该方言的参数值
#  错误码链接：https://www.xfyun.cn/document/error-code （code返回错误码时必看）
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import websocket
import datetime
import hashlib
import base64
import hmac
import json
from urllib.parse import urlencode
import time
import ssl
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import _thread as thread
import os
import numpy as np
import pandas as pd
import csv
from pydub import AudioSegment
STATUS_FIRST_FRAME = 0  # 第一帧的标识
STATUS_CONTINUE_FRAME = 1  # 中间帧标识
STATUS_LAST_FRAME = 2  # 最后一帧的标识

path =os.path.abspath('..')
path =os.path.dirname(path)
path1 =os.path.dirname(path)
print(path1)

class Ws_Param(object):
    # 初始化
    def __init__(self, APPID, APIKey, APISecret, AudioFile):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        self.AudioFile = AudioFile

        # 公共参数(common)
        self.CommonArgs = {"app_id": self.APPID}
        # 业务参数(business)，更多个性化参数可在官网查看
        # self.BusinessArgs = {"domain": "iat", "language": "zh_cn", "accent": "mandarin", "vinfo":1,"vad_eos":10000}
        self.BusinessArgs = {"domain": "iat", "language": "en_us", "vad_eos":2000}

    # 生成url
    def create_url(self):
        url = 'wss://ws-api.xfyun.cn/v2/iat'
        # url = 'wss://iat-api.xfyun.cn/v2/iat?authorization=YXBpX2tleT0ia2V5eHh4eHh4eHg4ZWUyNzkzNDg1MTlleHh4eHh4eHgiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iSHAzVHk0WmtTQm1MOGpLeU9McFFpdjlTcjVudm1lWUVIN1dzTC9aTzJKZz0i&date=Wed%2C%2010%20Jul%202019%2007%3A35%3A43%20GMT&host=iat-api.xfyun.cn'
        # 生成RFC1123格式的时间戳
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        # 拼接字符串
        signature_origin = "host: " + "ws-api.xfyun.cn" + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + "/v2/iat " + "HTTP/1.1"
        # 进行hmac-sha256进行加密
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()
        signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')

        authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
            self.APIKey, "hmac-sha256", "host date request-line", signature_sha)
        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
        # 将请求的鉴权参数组合为字典
        v = {
            "authorization": authorization,
            "date": date,
            "host": "ws-api.xfyun.cn"
        }
        # 拼接鉴权参数，生成url
        url = url + '?' + urlencode(v)
        # print("date: ",date)
        # print("v: ",v)
        # 此处打印出建立连接时候的url,参考本demo的时候可取消上方打印的注释，比对相同参数时生成的url与自己代码生成的url是否一致
        # print('websocket url :', url)
        return url


# 收到websocket消息的处理
def on_message(ws, message):
    try:
        code = json.loads(message)["code"]
        sid = json.loads(message)["sid"]
        global result
        if code != 0:
            errMsg = json.loads(message)["message"]
            print("sid:%s call error:%s code is:%s" % (sid, errMsg, code))
            # with open(filename, 'a') as file_object:
            #     file_object.write("KDXF could not understand audio!" + '\n')
        else:                      
            data = json.loads(message)["data"]["result"]["ws"]
            result = ""
            for i in data:
                for w in i["cw"]:
                    result += w["w"]
            # print("sid:%s call success!,data is:%s" % (sid, json.dumps(data, ensure_ascii=False)))
            # result = result.replace("\n", "")
            print(result)
            #print(type(result))
    except Exception as e:
        print("receive msg,but parse exception:", e)


# 收到websocket错误的处理
def on_error(ws, error):
    print("### error:", error)


# 收到websocket关闭的处理
def on_close(ws):
    print("### closed ###")


# 收到websocket连接建立的处理
def on_open(ws):
    def run(*args):
        frameSize = 8000  # 每一帧的音频大小
        intervel = 0.04  # 发送音频间隔(单位:s)
        status = STATUS_FIRST_FRAME  # 音频的状态信息，标识音频是第一帧，还是中间帧、最后一帧

        with open(wsParam.AudioFile, "rb") as fp:
            while True:
                buf = fp.read(frameSize)
                # 文件结束
                if not buf:
                    status = STATUS_LAST_FRAME
                # 第一帧处理
                # 发送第一帧音频，带business 参数
                # appid 必须带上，只需第一帧发送
                if status == STATUS_FIRST_FRAME:

                    d = {"common": wsParam.CommonArgs,
                         "business": wsParam.BusinessArgs,
                         "data": {"status": 0, "format": "audio/L16;rate=16000",
                                  "audio": str(base64.b64encode(buf), 'utf-8'),
                                  "encoding": "lame"}}
                    d = json.dumps(d)
                    ws.send(d)
                    status = STATUS_CONTINUE_FRAME
                # 中间帧处理
                elif status == STATUS_CONTINUE_FRAME:
                    d = {"data": {"status": 1, "format": "audio/L16;rate=16000",
                                  "audio": str(base64.b64encode(buf), 'utf-8'),
                                  "encoding": "lame"}}
                    ws.send(json.dumps(d))
                # 最后一帧处理
                elif status == STATUS_LAST_FRAME:
                    d = {"data": {"status": 2, "format": "audio/L16;rate=16000",
                                  "audio": str(base64.b64encode(buf), 'utf-8'),
                                  "encoding": "lame"}}
                    ws.send(json.dumps(d))
                    time.sleep(1)
                    break
                # 模拟音频采样间隔
                time.sleep(intervel)
        ws.close()

    thread.start_new_thread(run, ())


# audio_add_list = []
# text_add_list = []
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
path = os.path.join(path+r"\kdxf.csv")

origin_result = []
phasevoctor_result = []
ola_result = []
wsola_result = []
def kdxf_asr(audio, filename):
    global wsParam
    # APPID='5e4936be', APIKey='a1d59fcb877819cf203e7ce804d248a4',APISecret='0c54ef03a106903edf9b9fce4e82cbc9'
    wsParam = Ws_Param(APPID='5e6dbb5d', APIKey='9958a244dd66c20854c98e4b6e359530',
        APISecret='62d36bbf3ac95ad860f447def4518d1c',
        AudioFile= audio )
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()
    ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    # with open(output_add) as output_add_object:
    #     for text_add in output_add_object:
    #         text_add = text_add.strip()
    #将ASR识别结果写入文件
    if (audio == audio_origin):
        origin_result.append(result.lower())
    elif (audio == audio_phasevoctor):
        phasevoctor_result.append(result.lower())
    elif (audio == audio_ola):
        ola_result.append(result.lower())
    elif (audio == audio_wsola):
        wsola_result.append(result.lower())
        
    # with open(filename, 'a') as file_object:
    #     file_object.write(result + '\n')

if __name__ == "__main__":
    # 测试时候在此处正确填写相关信息即可运行
    num = 0#choose one of the ten origin speech

    for i in np.arange(0.25, 3, 0.25):
        for num in range(0, 10):
            num +=1
            # audio_origin = 'C:/Users/73936/Desktop/voice_speech/dataset/' + str(num) +'.wav'
            # kdxf_asr_origin = 'C:/github_code/audio_tsm_test/test_result/kdxf/kdxf_origin.txt'
            # kdxf_asr(audio_origin, kdxf_asr_origin)
            audio_origin =  path1 + '/dataset/speech_origin/without_wake_words/16k/' + str(num) +'.mp3'
            kdxf_asr_origin = path1 + '/test_result/kdxf/16k/without_wake_words/kdxf_origin.txt'

            ### voice with wake words
            # audio_phasevoctor = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/phasevoctor' + str(i) + '_' + str(num) +'.wav'
            # audio_ola = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/ola' + str(i) + '_' + str(num) +'.wav'
            # audio_wsola = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/wsola' + str(i) + '_' + str(num) +'.wav'
           
            # # google_asr_origin = 'C:/github_code/audio_tsm_test/test_result/google_origin.txt'
            # kdxf_asr_phasevoctor = 'C:/github_code/audio_tsm_test/test_result/kdxf/kdxf_asr_phasevoctor' + str(i) + '.txt'
            # kdxf_asr_ola = 'C:/github_code/audio_tsm_test/test_result/kdxf/kdxf_asr_ola' + str(i) + '.txt'
            # kdxf_asr_wsola = 'C:/github_code/audio_tsm_test/test_result/kdxf/kdxf_asr_wsola' + str(i) + '.txt'
            
            ### voice without wake words
            audio_phasevoctor = path1 + '/dataset/16k/without_wake_words/phasevoctor' + str(i) + '_' + str(num) +'.mp3'
            audio_ola = path1 + '/dataset/16k/without_wake_words/ola' + str(i) + '_' + str(num) +'.mp3'
            audio_wsola = path1 + '/dataset/16k/without_wake_words/wsola' + str(i) + '_' + str(num) +'.mp3'
           
            # google_asr_origin = 'C:/github_code/audio_tsm_test/test_result/google_origin.txt'
            kdxf_asr_phasevoctor = path1 + '/test_result/kdxf/16k/without_wake_words/kdxf_asr_phasevoctor' + str(i) + '.txt'
            kdxf_asr_ola = path1 + '/test_result/kdxf/16k/without_wake_words/kdxf_asr_ola' + str(i) + '.txt'
            kdxf_asr_wsola = path1 + '/test_result/kdxf/16k/without_wake_words/kdxf_asr_wsola' + str(i) + '.txt'
            if(i == 0.25):
                kdxf_asr(audio_origin, kdxf_asr_origin)
            kdxf_asr(audio_phasevoctor, kdxf_asr_phasevoctor)
            kdxf_asr(audio_ola, kdxf_asr_ola)
            kdxf_asr(audio_wsola, kdxf_asr_wsola)
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
    print('successfully')
             
        
