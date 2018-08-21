#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/17 15:54
# @Author  : yixiong

import urllib3
import requests
import json

class user_feedback():    #用户反馈
    def user_feedback():
        headers = {
            'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1MDEiLCJzdWIiOiI1YWMzNDRiOGJjOGU3NzAwMDVmNzJjZTkiLCJpYXQiOjE1MzM4MDk4MzA0NjEsImV4cCI6MTUzMzgzNTAzMDQ2MX0.NVJsKhRmrnve-6pMlSMto4CesFKY8N6RGpCurqzWvCY',
            'Content-Type': 'application/json'
            }
        url = 'https://test-wechatapp.intbee.com/api/user/feedback'
        data = {
            'content':'cesces',
            'userUuid':'5ac344b8bc8e770005f72ce9'
            }
        data_json = json.dumps(data)
        req = requests.post(url, headers = headers, data = data_json)
        user_text = req.text
        user_json = req.json()

        if user_json['code'] == 0:
            print('Ture, user feedback is OK')
        else:
            print('Flase')
            print(user_text)
