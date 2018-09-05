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


class user_feedback():    #用户反馈
    def user_feedback():
        headers = BaseRequest.headers
        url = str(BaseRequest.url) + '/user/feedback'
        data = {
            'content':'cesces',
            'userUuid':'5ac344b8bc8e770005f72ce9'
            }
        data_json = json.dumps(data)
        req = requests.post(url, headers = headers, data = data_json)
        user_text = req.text
        user_json = req.json()

        if user_json['code'] == 0:
            print('Ture, user feedback is OK')
        else:
            print('Flase')
            print(user_text)

