#-*- coding: UTF-8 -*-
#人脸美妆

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
    rsp = ai_obj.getfacecosmetic(image_data,1)

    if rsp['ret'] == 0:
        strs = rsp['data']['image']
        imgdata = base64.b64decode(strs)
        file = open('../data/f-4-m.jpg', 'wb')
        file.write(imgdata)
        file.close()
        print '----------------------API SUCC----------------------'
    else:
        print json.dumps(rsp, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
        print '----------------------API FAIL----------------------'

'''
编码	类型	    名称	        效果	    
1	日系妆	芭比粉	日系妆 - 芭比粉  	    
2	日系妆	清透	    日系妆 - 清透    	        
3	日系妆	烟灰	    日系妆 - 烟灰    	        
4	日系妆	自然	    日系妆 - 自然    	        
5	日系妆	樱花粉	日系妆 - 樱花粉  	    
6	日系妆	原宿红	日系妆 - 原宿红  	    
7	韩妆	    闪亮	    韩妆   - 闪亮    	            
8	韩妆	    粉紫	    韩妆   - 粉紫    	        
9	韩妆	    粉嫩	    韩妆   - 粉嫩           	
10	韩妆	    自然	    韩妆   - 自然           	
11	韩妆	    清透  	韩妆   - 清透           
12	韩妆	    大地色	韩妆   - 大地色 
13	韩妆	    玫瑰	    韩妆   - 玫瑰 	
14	裸妆	    自然	    裸妆   - 自然		
15	裸妆	    清透	    裸妆   - 清透
16	裸妆	    桃粉	    裸妆   - 桃粉
17	裸妆	    橘粉	    裸妆   - 橘粉
18	裸妆	    春夏	    裸妆   - 春夏
19	裸妆	    秋冬	    裸妆   - 秋冬
20	主题妆	经典复古	主题妆 - 经典复古
21	主题妆	性感混血	主题妆 - 性感混血
22	主题妆	炫彩明眸	主题妆 - 炫彩明眸
23	主题妆	紫色魅惑	主题妆 - 紫色魅惑
'''