#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/17 15:54
# @Author  : yixiong

import urllib3
import requests
import json

class add_product():   #添加商品
    def add():
        headers = {
            'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1MDEiLCJzdWIiOiI1YWMzNDRiOGJjOGU3NzAwMDVmNzJjZTkiLCJpYXQiOjE1MzM4MDk4MzA0NjEsImV4cCI6MTUzMzgzNTAzMDQ2MX0.NVJsKhRmrnve-6pMlSMto4CesFKY8N6RGpCurqzWvCY',
            'Content-Type': 'application/json'
            }
        data = {
            "merchant_uuid":"5ac344b8bc8e770005f72ce9",
            "title": "测试123",
            "main_image": [        
                "http://miniprogram-static.intbee.com/FjPqv_lP8pYRGOr4pDF_CY7wu2i9",
                "http://miniprogram-static.intbee.com/Fjc6YVEbkyO96TBkYyBLKxxv8a8K",
                "http://miniprogram-static.intbee.com/Fq1tJDnJXmfHASHzME7B59HYzEv6"],
            "price": "0.01",
            "stock": "12",
            "product_status":"0",
            "description": "[{\"text\":\"恶魔一组图\",\"image\":\"http://miniprogram-static.intbee.com/Fjc6YVEbkyO96TBkYyBLKxxv8a8K\"}]"
          }
        data_json = json.dumps(data)
        url = 'https://test-wechatapp.intbee.com/api/product'
        req = requests.post(url,headers = headers,data=data_json)
        user_text = req.text
        user_json = json.loads(user_text)

        if user_json['code'] == 0:
            print('Ture, add product is OK')
        else:
            print('Flase')
            print(user_text)
   
        