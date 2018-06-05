#-*- coding: UTF-8 -*-
#人脸分析

import sys
sys.path.append('../SDK')
import optparse
import time
import apiutil
import base64
import json

app_key = 'T1Gj1V8hwZmmxgE1'
app_id = '1106866541'

if __name__ == '__main__':
    with open('../data/f-4.jpg', 'rb') as bin_data:
        image_data = bin_data.read()

    ai_obj = apiutil.AiPlat(app_id, app_key)

    print '----------------------SEND REQ----------------------'
    rsp = ai_obj.getdetectface(image_data)

    if rsp['ret'] == 0:
        for obj in rsp['data']['face_list']:
            print "性别:", obj['gender']
            print "年龄:", obj['age']
            print "情感:", obj['expression']
            print "魅力:", obj['beauty']
            #print "眼镜:", obj['glass']
        print '----------------------API SUCC----------------------'
    else:
        print json.dumps(rsp, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
        print '----------------------API FAIL----------------------'
