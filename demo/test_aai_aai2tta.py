#-*- coding: UTF-8 -*-
#语音转文字

import os
import sys
sys.path.append('../SDK')  
import optparse
import time
import apiutil
import json
import base64

app_key = 'T1Gj1V8hwZmmxgE1'
app_id = '1106866541'

if __name__ == '__main__':
    str_text = '在饭店和女朋友提分手，她伤心的哭了。在场的所有人都以为我在求婚——于是掌声响了起来。'
    #str_text = '哈喽!我是迪森,你可以用文字或者语音和我聊天,也可以发给我图片,我给你分析美化一下' #UTF-8编码，非空且长度上限150字节
    ai_obj = apiutil.AiPlat(app_id, app_key)

    print '----------------------SEND REQ----------------------'
    rsp = ai_obj.getAaiToTts(str_text) #普通话男声	1  静琪女声	5  欢馨女声	6  欢馨女声	6
    if rsp['ret'] == 0:
        #str = rsp['data']['speech']
        str = rsp['data']['voice']
        speech_chunk = base64.b64decode(str)
        file = open('../data/text.amr', 'wb')
        file.write(speech_chunk)
        file.close()
        print '----------------------API SUCC----------------------'
    else:
        print json.dumps(rsp, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
        # print rsp
        print '----------------------API FAIL----------------------'

