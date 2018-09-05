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

class merchant_amount_log():   #账单明细
    def amount_log():
        headers = BaseRequest.headers
        url = BaseRequest.url + '/merchant/amount/log'
        req = requests.get(url ,headers = headers)
        user_text = req.text
        user_json = req.json()

        if user_json['code'] == 0:
            print('Ture, merchant amount log  is OK')
        else:
            print('Flase')
            print(user_text)
            
        