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

class order_agree_refund():   #同意退款
    def agree_refund():
        headers = BaseRequest.headers
        url = BaseRequest.url + '/order/75/agree/refund'
        req = requests.post(url ,headers = headers)
        user_text = req.text
        user_json = req.json()

        if user_json['code'] == 0:
            print('Ture, order agree refund is OK')
        else:
            print('Flase')
            print(user_text)
            
        