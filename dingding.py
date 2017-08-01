#coding: utf-8
import json,urllib2

url = "https://oapi.dingtalk.com/robot/send?access_token=3576aa63ffb6f9ab55cb1d54cebadfd16c847da0824328d890ae38904eee7"

header = {
    "Content-Type": "application/json",
    "charset": "utf-8"
    }

data = {

     "msgtype": "text", 
        "text": {
            "content": "1111111111111111"
        },
#@人员，非必须
     "at": {
            "isAtAll":True
         }
    }




#发送格式必须为json格式，不然发送不成功。
sendData = json.dumps(data)

request = urllib2.Request(url,data = sendData,headers = header)
urlopen = urllib2.urlopen(request)
print urlopen.read()

