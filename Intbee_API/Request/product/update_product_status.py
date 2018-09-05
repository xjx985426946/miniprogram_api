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

class update_produt_status():   #更新商品状态
    def update_status():
        headers = BaseRequest.headers
        url = str(BaseRequest.url) + '/product/5ac344b8bc8e770005f72ce9/35/2'
        req = requests.put(url,headers = headers)
        user_text = req.text
        user_json = req.json()

        if user_json['code'] == 0:
            print('Ture, update product status is OK')
        else:
            print('Flase')
            print(user_text)

