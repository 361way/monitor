#!/usr/bin/env python
#coding=utf-8
#调用dingding接口，通过post API，传参tokenid和要发送的告警内容

import json,urllib2,sys

def usage():
    '''usage'''
    print 'Usage: %s %s %s' %(sys.argv[0],'tokenid','Message')
    sys.exit()


def dingding(tokenid,message):
    url = "https://oapi.dingtalk.com/robot/send?access_token=" + tokenid

    header = {
        "Content-Type": "application/json",
        "charset": "utf-8"
        }

    data = {

         "msgtype": "text",
            "text": {
                "content": message
            }
        }

    sendData = json.dumps(data)
    request = urllib2.Request(url,data = sendData,headers = header)
    urlopen = urllib2.urlopen(request)
    return urlopen.read()

def main():
    if len(sys.argv) != 3:
        usage()
    tokenid = sys.argv[1]
    message = sys.argv[2]
    dingding(tokenid, message)

if __name__ == "__main__":
    main()
