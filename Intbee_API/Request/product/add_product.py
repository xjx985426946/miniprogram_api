#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/17 15:54
# @Author  : yixiong

import urllib3
import requests
import json
import sys
sys.path.append("../base/")
from base_request import BaseRequest

class add_product():   #添加商品
    def add():
        headers = BaseRequest.headers
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
        url = str(BaseRequest.url) + '/product'
        req = requests.post(url,headers = headers,data=data_json)
        user_text = req.text
        user_json = req.json()

        if user_json['code'] == 0:
            print('Ture, add product is OK')
        else:
            print('Flase')
            print(user_text)
   
        