#-*- coding: UTF-8 -*-
#物体识别

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
    with open('../data/place-2.jpg', 'rb') as bin_data:
        image_data = bin_data.read()

    ai_obj = apiutil.AiPlat(app_id, app_key)

    print '----------------------SEND REQ----------------------'
    rsp = ai_obj.getvision_objectr(image_data,1) #返回结果个数（已按置信度倒排）
    if rsp['ret'] == 0:
        for obj in rsp['data']['object_list']:
            print "物体标签: ",obj['label_id']
            print "置信度  : ",obj['label_confd']

        print '----------------------API SUCC----------------------'
    else:
        print json.dumps(rsp, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
        print '----------------------API FAIL----------------------'

