# -*- coding: utf-8 -*-
# Created by apple on 2017/2/17.

from Request.base.base_intbee_request import BaseInebeeRequest
from Request.user_center.register import RegisterV1, RegisterV1Param
from Request.user_center.login import Login, Login_param
from Request.user_center.api_login import api_login,api_login_param
import json
import requests
import config

__token = None
__token_key = 'access_token'
mobile = None
cookies = None
headers = {}

def regiset():
    def wrapper(func):
        def _wrapper(*args, **kwargs):
            global __token,mobile
            if not __token:
                param = Login_param.defult()
                params = json.dumps(param.dict)
                print(params)
                respone = Login.request(params)
                respone_text = respone.text
                text_dict = json.loads(respone_text)
                __token = text_dict['result']['access_token']
                mobile = text_dict['result']['credential_key']
                # session = BaseInebeeRequest.session
                # session.headers.update({__token_key: token})
                BaseInebeeRequest.headers.update({__token_key: __token})
                BaseInebeeRequest.headers.update({"mobile":mobile})
                # print(BaseInebeeRequest.headers)
                # session.headers.update({version:version})
            func(*args, **kwargs)
        return _wrapper
    return wrapper

def login():
    def wrapper(func):
        def _wrapper(*args, **kwargs):
            global __token,mobile,headers
            data = {"mobile":"13676055719","password":"e10adc3949ba59abbe56e057f20f883e"}
            data = json.dumps(data)
            header = {"Content-Type": "application/json"}
            url = str(config.m_host['host']) + '/auth/signin/manufacture'
            session = requests.session()
            print(url,data,header)
            response = session.post(url=url, data=data, headers=header)
            print(response.text)
            # print(response.text)
            cookie = response.cookies
            session = str(cookie.get('SHAREJSESSIONID'))
            cookies = 'SHAREJSESSIONID=' + session
            headers.update({"Cookie":cookies})
            headers.update({"Content-Type":"application/json"})
            BaseInebeeRequest.headers.update({"Cookie":cookies})
            func(*args, **kwargs)
        return _wrapper
    return wrapper

def apilogin():
    def wrapper(func):
        def _wrapper(*args, **kwargs):
            global __token,mobile
            data = {"grant_type":"password","credential":"+86-13676055719","app_id":"101","app_secret":"","platform":"iOS","password":"e10adc3949ba59abbe56e057f20f883e"}
            data = json.dumps(data)
            header = {"Content-Type": "application/json","platform":"iOS","version":"22000"}
            url = config.host_api['host'] + '/api/v1/signin'
            session = requests.session()
            respone = session.post(url=url,data=data,headers=header)
            respone_dict = json.loads(respone.text)
            print(respone_dict)
            access_token = respone_dict['result']['access_token']
            headers.update({'access_token':access_token})
            headers.update({"Content-Type":"application/json","platform":"iOS","version":"22000"})
            BaseInebeeRequest.headers.update({"access_token":access_token,"Content-Type": "application/json","platform":"iOS","version":"21000"})
            func(*args, **kwargs)
        return _wrapper
    return wrapper

def ccc_login():
    def wrapper(func):
        def _wrapper(*args,**kwargs):
            global __token
            param = '{"username": "13676055719", "password": "e10adc3949ba59abbe56e057f20f883e"}'
            headers = {"Content-Type":"application/json"}
            print(config.host)
            url = str(config.host['host']) + '/api/square/v1/session/signin'
            session = requests.session()
            response = session.post(url=url,data=param,headers=headers)
            print(response.text)
            response_dict = json.loads(response.text)
            Authorization = 'bearer ' + str(response_dict['result']['access_token'])
            BaseInebeeRequest.headers.update({"Authorization": Authorization})
            func(*args, **kwargs)
        return _wrapper
    return wrapper

def logout(func):
    def wrapper(*args, **kwargs):
        # BaseInebeeRequest.session.headers.pop(__token_key)
        # BaseInebeeRequest.headers.pop(__token_key)
        func(*args, **kwargs)
    return wrapper

if __name__ == "__main__":
    login()