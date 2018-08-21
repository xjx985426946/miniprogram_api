#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/17 15:54
# @Author  : yixiong

import urllib3
import requests
import json

class product_details():   #获取商品详情
    def details():
        headers = {
            'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1MDEiLCJzdWIiOiI1YWMzNDRiOGJjOGU3NzAwMDVmNzJjZTkiLCJpYXQiOjE1MzM4MDk4MzA0NjEsImV4cCI6MTUzMzgzNTAzMDQ2MX0.NVJsKhRmrnve-6pMlSMto4CesFKY8N6RGpCurqzWvCY'
            }
        url = 'https://test-wechatapp.intbee.com/api/product/31'
        req = requests.get(url ,headers = headers)
        user_text = req.text
        user_json = req.json()

        if user_json['code'] == 0:
            print('Ture, product details is OK')
        else:
            print('Flase')
            print(user_text)
            
        
        