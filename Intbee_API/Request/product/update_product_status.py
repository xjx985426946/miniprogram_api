#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/17 15:54
# @Author  : yixiong

import urllib3
import requests
import json

class update_produt_status():   #更新商品状态
    def update_status():
        headers = {
            'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1MDEiLCJzdWIiOiI1YWMzNDRiOGJjOGU3NzAwMDVmNzJjZTkiLCJpYXQiOjE1MzM4MDk4MzA0NjEsImV4cCI6MTUzMzgzNTAzMDQ2MX0.NVJsKhRmrnve-6pMlSMto4CesFKY8N6RGpCurqzWvCY',

            }

        url = 'https://test-wechatapp.intbee.com/api/product/5ac344b8bc8e770005f72ce9/35/2'
        req = requests.put(url,headers = headers)
        user_text = req.text
        user_json = req.json()

        if user_json['code'] == 0:
            print('Ture, update product status is OK')
        else:
            print('Flase')
            print(user_text)

