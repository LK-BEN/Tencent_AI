#-*- coding: UTF-8 -*-
#文字翻译

import sys
sys.path.append('../SDK')  
import optparse
import time
import apiutil
import json

app_key = 'T1Gj1V8hwZmmxgE1'
app_id = '1106866541'

if __name__ == '__main__':
    with open('../data/generalocr.jpg', 'rb') as bin_data:
        image_data = bin_data.read()

    ai_obj = apiutil.AiPlat(app_id, app_key)

    print '----------------------SEND REQ----------------------'
    rsp = ai_obj.getNlpImageTrans(image_data)
    if rsp['ret'] == 0:
        for obj in rsp['data']['image_records']:
            print "源文本: ", obj['source_text']
            print "译文本: ", obj['target_text']

        print '----------------------API SUCC----------------------'
    else:
        print json.dumps(rsp, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
        # print rsp
        print '----------------------API FAIL----------------------'

