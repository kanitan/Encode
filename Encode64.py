# -*- encoding: utf-8 -*-
'''
@File: Encode64.py
@Describe: 
@Create Time: 2020/05/27 15:07:10
@Author: Lookback
@Version: 1.0
'''

import base64
import urllib.parse


message = "Python is fun"
base64_message = 'UHl0aG9uIGlzIGZ1bg=='
url_message = '%28%29'
hex_message = '(?i)[\s\"\'`;\/0-9=\x0B\x09\x0C\x3B\x2C\x28\x3B]on[a-zA-Z]+[\s\x0B\x09\x0C\x3B\x2C\x28\x3B]*?='

#base64 encode 
def base64_encode(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print('\nbase64 encode result:',base64_message)

#base64 decode
def base64_decode(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print('base64 decode result:',repr(message),'\n')

#url decode
def url_encode(message):
    print('url encode result:',urllib.parse.quote(message))

#url encode
def url_decode(url_message):
    print('url decode result:',urllib.parse.unquote(url_message),'\n')

#hex encode
def hex_encode(message):
    print('hex decode result:',message.encode('ascii').hex())

def hex_decode(hex_message):
    print('hex decode result:',repr(str(hex_message)))

if __name__ == "__main__":
    base64_encode(message)
    base64_decode(base64_message)
    url_encode(message)
    url_decode(url_message)
    hex_encode(message)
    hex_decode(hex_message)

