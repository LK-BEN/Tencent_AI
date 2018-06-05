#-*- coding: UTF-8 -*-
#画面描述

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
    with open('../data/place-4.jpg', 'rb') as bin_data:
        image_data = bin_data.read()

    ai_obj = apiutil.AiPlat(app_id, app_key)

    print '----------------------SEND REQ----------------------'
    rsp = ai_obj.gevision_imgtotext(image_data,'dsklanvlkasdd')
    if rsp['ret'] == 0:
        #print json.dumps(rsp, ensure_ascii=False)
        #for obj in rsp['data']:
        #    print '  画面描述： ',rsp['data'][obj]
        print '  画面描述： ', rsp['data']['text']
        print '----------------------API SUCC----------------------'
    else:
        print json.dumps(rsp, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
        print '----------------------API FAIL----------------------'
