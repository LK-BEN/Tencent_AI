# -*- coding: UTF-8 -*-
#人脸变妆

import os
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
        image_data = bin_data.read()        #原始图片的base64编码数据（原图大小上限500KB)

    ai_obj = apiutil.AiPlat(app_id, app_key)

    print '----------------------SEND REQ----------------------'
    rsp = ai_obj.getfacedecoration(image_data,2)

    if rsp['ret'] == 0:
        strs = rsp['data']['image']
        imgdata = base64.b64decode(strs)
        file = open('../data/f-4-b.jpg', 'wb')
        file.write(imgdata)
        file.close()
        print '----------------------API SUCC----------------------'
    else:
        print json.dumps(rsp, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
        print '----------------------API FAIL----------------------'

'''
编码	 名称	 效果	            编码	  名称	     效果
1	埃及妆	埃及妆            	2	巴西土著妆	巴西土著妆        
3	灰姑娘妆	灰姑娘妆          	4	恶魔妆	    恶魔妆            
5	武媚娘妆	武媚娘妆          	6	星光薰衣草	星光薰衣草        
7	花千骨	花千骨            	8	僵尸妆	    僵尸妆            
9	爱国妆	爱国妆            	10	小胡子妆	    小胡子妆          
11	美羊羊妆	美羊羊妆          	12	火影鸣人妆	火影鸣人妆        
13	刀马旦妆	刀马旦妆          	14	泡泡妆	    泡泡妆            
15	桃花妆	桃花妆            	16	女皇妆	    女皇妆            
17	权志龙	权志龙            	18	撩妹妆	    撩妹妆            
19	印第安妆	印第安妆          	20	印度妆	    印度妆            
21	萌兔妆	萌兔妆            	22	大圣妆	    大圣妆            
'''