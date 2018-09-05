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

class order_carrier():   #订单发货
    def carrier():
        headers = BaseRequest.headers
        data = {
                "carrier_company":"申通快递",
                "carrier_no": "221340481292",
                "carrier_company_no":"STO"
            }
        data_json = json.dumps(data)
        url = BaseRequest.url + '/order/75/carrier'
        req = requests.post(url ,headers = headers,data=data_json)
        user_text = req.text
        user_json = req.json()

        if user_json['code'] == 0:
            print('Ture, order carrier is OK')
        else:
            print('Flase')
            print(user_text)
            
        