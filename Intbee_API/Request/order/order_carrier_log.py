#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/17 15:54
# @Author  : yixiong

import urllib3
import requests
import json

class order_carrier_log():   #订单物流轨迹查询
    def carrier_log():
        headers = {
            'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1MDEiLCJzdWIiOiI1YWMzNDRiOGJjOGU3NzAwMDVmNzJjZTkiLCJpYXQiOjE1MzM4MDk4MzA0NjEsImV4cCI6MTUzMzgzNTAzMDQ2MX0.NVJsKhRmrnve-6pMlSMto4CesFKY8N6RGpCurqzWvCY'
            }
        url = 'https://test-wechatapp.intbee.com/api/order/78/carrier/logistic/'
        req = requests.get(url ,headers = headers)
        user_text = req.text
        user_json = json.loads(user_text)

        if user_json['code'] == 0:
            print('Ture, order list is OK')
        else:
            print('Flase')
            print(user_text)
            
