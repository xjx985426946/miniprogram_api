#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/17 15:54
# @Author  : yixiong

import urllib3
import requests
import json

class user_delete_follow():   #取消已关注商家
    def delete_follow():
        headers = {
            'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1MDEiLCJzdWIiOiI1YWMzNDRiOGJjOGU3NzAwMDVmNzJjZTkiLCJpYXQiOjE1MzM4MDk4MzA0NjEsImV4cCI6MTUzMzgzNTAzMDQ2MX0.NVJsKhRmrnve-6pMlSMto4CesFKY8N6RGpCurqzWvCY'
            }
        url = 'https://test-wechatapp.intbee.com/api/user/5ac344b8bc8e770005f72ce9/followMerchant?uuid=5b0e5f2b53bbc10005380ca6'
        req = requests.delete(url,headers = headers)
        user_text = req.text
        user_json = req.json()

        if user_json['code'] == 0:
            print('Ture, user delete follow is OK')

        else:
            print('Flase')
            print(user_text)
        

        