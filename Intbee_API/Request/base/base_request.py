#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/13 16:15
# @Author  : yixiong

import json
import requests




class BaseRequest:
    """
    基础请求
    """
    url = 'https://test-wechatapp.intbee.com/api'
    protocol = ''  # 协议 http https
    host = ''  # 服务器地址
    port = '80'  # 服务器端口, default 80
    method = 'POST'  # 请求方法 GET POST DELETE PUT ..., default POST
    headers = {'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1MDEiLCJzdWIiOiI1YWMzNDRiOGJjOGU3NzAwMDVmNzJjZTkiLCJpYXQiOjE1MzM4MDk4MzA0NjEsImV4cCI6MTUzMzgzNTAzMDQ2MX0.NVJsKhRmrnve-6pMlSMto4CesFKY8N6RGpCurqzWvCY'}


