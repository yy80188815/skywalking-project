import time

import requests

from warp import async_decorator


@async_decorator
def get_baidu():
    requests.get("http://127.0.0.1:9080/baidu")

@async_decorator
def get_douban():
    requests.get("http://127.0.0.1:9081/douban")

@async_decorator
def get_douyin():
    requests.get("http://127.0.0.1:9082/douyin")

@async_decorator
def get_taobao():
    requests.get("http://127.0.0.1:9083/taobao")

@async_decorator
def get_xiaohongshu():
    requests.get("http://127.0.0.1:9084/xiaohongshu")

@async_decorator
def get_data():
    requests.get("http://127.0.0.1:9085/data")
get_baidu()
get_douban()
while True:
    get_baidu()
    get_douban()
    # get_douyin()
    # get_taobao()
    # get_xiaohongshu()
    # get_data()
    time.sleep(60)
