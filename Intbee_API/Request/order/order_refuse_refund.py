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

class order_refuse_refund():   #拒绝退款
    def refuse_refund():
        headers = BaseRequest.headers
        url = BaseRequest.url + '/order/75/refuse/refund'
        req = requests.post(url ,headers = headers)
        user_text = req.text
        user_json = req.json()

        if user_json['code'] == 0:
            print('Ture, order refuse refund is OK')
        else:
            print('Flase')
            print(user_text)
            
        