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


class user_add_follow():   #添加关注商家
    def add_follow():
        headers = BaseRequest.headers
        url = str(BaseRequest.url) + '/user/5ac344b8bc8e770005f72ce9/followMerchant?uuid=5b0e5f2b53bbc10005380ca6'
        req = requests.post(url ,headers = headers)
        user_text = req.text
        user_json = req.json()

        if user_json['code'] == 0:
            print('Ture, user add follow is OK')

        else:
            print('Flase')
            print(user_text)
        