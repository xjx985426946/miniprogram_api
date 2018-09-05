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


class user_follow():   #获取用户关注商家信息
    def follow():
        headers = BaseRequest.headers
        url =  str(BaseRequest.url) + '/user/5ac344b8bc8e770005f72ce9/followMerchant'
        req = requests.get(url ,headers = headers)
        user_text = req.text
        user_json = req.json()

        if user_json['code'] == 0:
            print('Ture, user follow is OK')
        else:
            print('Flase')
            print(user_text)

    