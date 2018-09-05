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

class add_address():   #新增/编辑收货地址
    def add_edit():
        headers = {
            'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1MDEiLCJzdWIiOiI1YWMzNDRiOGJjOGU3NzAwMDVmNzJjZTkiLCJpYXQiOjE1MzM4MDk4MzA0NjEsImV4cCI6MTUzMzgzNTAzMDQ2MX0.NVJsKhRmrnve-6pMlSMto4CesFKY8N6RGpCurqzWvCY',
            'Content-Type': 'application/json'
            }
        data = {
            "uuid":"5ac344b8bc8e770005f72ce9",
            "name": "测试",
            "phone": "13640993513",
            "province": "广东省",
            "city": "深圳市",
            "district": "南山区",
            "address": "讯美科技广场3号楼"
        } 
        data_json = json.dumps(data)
        
        url = 'https://test-wechatapp.intbee.com/api/address'
        req = requests.get(url ,headers = headers,data=data_json)
        user_text = req.text
        user_json = req.json()

        if user_json['code'] == 0:
            print('Ture, add address is OK')
        else:
            print('Flase')
            print(user_text)
            