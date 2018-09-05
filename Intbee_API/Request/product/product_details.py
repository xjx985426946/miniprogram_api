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

class product_details():   #获取商品详情
    def details():
        headers = BaseRequest.headers
        url = str(BaseRequest.url) + '/product/31'
        req = requests.get(url ,headers = headers)
        user_text = req.text
        user_json = req.json()

        if user_json['code'] == 0:
            print('Ture, product details is OK')
        else:
            print('Flase')
            print(user_text)
            
        
        