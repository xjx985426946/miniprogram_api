#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/17 15:54
# @Author  : yixiong

import urllib3
import requests
import json

class order_carrier():   #订单发货
    def carrier():
        headers = {
            'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1MDEiLCJzdWIiOiI1YWMzNDRiOGJjOGU3NzAwMDVmNzJjZTkiLCJpYXQiOjE1MzM4MDk4MzA0NjEsImV4cCI6MTUzMzgzNTAzMDQ2MX0.NVJsKhRmrnve-6pMlSMto4CesFKY8N6RGpCurqzWvCY'
            }
        data = {
                "carrier_company":"申通快递",
                "carrier_no": "221340481292",
                "carrier_company_no":"STO"
            }
        data_json = json.dumps(data)
        url = 'https://test-wechatapp.intbee.com/api/order/75/carrier'
        req = requests.post(url ,headers = headers,data=data_json)
        user_text = req.text
        user_json = req.json()

        if user_json['code'] == 0:
            print('Ture, order carrier is OK')
        else:
            print('Flase')
            print(user_text)
            
        