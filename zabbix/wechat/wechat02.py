#!/usr/bin/env python
# coding=utf8
# ===============================================================================
#   Copyright (C) 2019 www.361way.com site All rights reserved.
#   
#   Filename      ：wechat02.py
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2019-06-21 17:55
#   Description   ：
# ===============================================================================
#!/usr/bin/env python
# encoding: utf-8

import urllib,urllib2
import json
import sys
#import simplejson
reload(sys)
sys.setdefaultencoding('utf8')

def gettoken(corpid,corpsecret):
    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
    print  gettoken_url
    try:
        token_file = urllib2.urlopen(gettoken_url)
    except urllib2.HTTPError as e:
        print e.code
        print e.read().decode("utf8")
        sys.exit()
    token_data = token_file.read().decode('utf-8')
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    return token


def senddata(access_token,user,subject,content):

    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
    send_values = {
        "touser":user,    #企业号中的用户帐号，在zabbix用户Media中配置，如果配置不正常，将按部门发送。
        "toparty":"",     #企业号中的部门id。
        "msgtype":"text", #消息类型。
        "agentid":"1000002",    #企业号中的应用id。
        "text":{
            "content":subject + '\n' + content
           },
        "safe":"0"
        }
    send_data = json.dumps(send_values, ensure_ascii=False)
#    send_data = simplejson.dumps(send_values, ensure_ascii=False).encode('utf-8')
    send_request = urllib2.Request(send_url, send_data)
    response = json.loads(urllib2.urlopen(send_request).read())
    print str(response)

if __name__ == '__main__':
    user = str(sys.argv[1])     #zabbix传过来的第一个参数
    subject = str(sys.argv[2])  #zabbix传过来的第二个参数
    content = str(sys.argv[3])  #zabbix传过来的第三个参数

    corpid =  'xxxxxxxxxxx'   #CorpID是企业号的标识
    corpsecret = 'xxxxxxxxxxxxxxxxxx'  #corpsecretSecret是管理组凭证密钥
    try:
        accesstoken = gettoken(corpid,corpsecret)
        senddata(accesstoken,user,subject,content)
    except Exception as e:
        print 'Exception: ', e
