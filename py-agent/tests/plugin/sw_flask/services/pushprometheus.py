#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import time

from flask import Flask, Response
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

from mysql_connect import MysqlTaskConfig

app = Flask(__name__)

mysqldb = MysqlTaskConfig.get_instance()
#@app.route('/metrics')
def get_data(server):
    timeend = int(time.time()) - 300
    sql = "select * from f_spider_data_test where f_servername='{}' and f_created_at > {}".format(server, timeend)
    return mysqldb.mysql_data_read(sql)

def send_metrics(servername,timetype,metricname):
    registry = CollectorRegistry()
    baidu_result = get_data("zhongshan")
    baidu_result = ["1","2"]
    print(servername + ":%s" % str(len(baidu_result)))
    #baidu_result = 15
    if baidu_result:
        gauge_baidu = Gauge(metricname, 'an example showed how to use gauge', ['job',"timetype"], registry=registry)
        gauge_baidu.labels(servername,timetype).set(len(baidu_result))
        push_to_gateway("172.17.2.64:9091", job=servername, registry=registry)

def hello():
    send_metrics("baidu","1","spider_count")
    send_metrics("douban","1","spider_count")
    send_metrics("douyin","1","spider_count")
    send_metrics("taobao","1","spider_count")
    send_metrics("xiaohongshu","1","spider_count")
    send_metrics("baidu_cpu","1","spider_cpu")
    send_metrics("douban_cpu","1","spider_cpu")
    send_metrics("douyin_cpu","1","spider_cpu")
    send_metrics("taobao_cpu","1","spider_cpu")
    send_metrics("xiaohongshu_cpu","1","spider_cpu")
    send_metrics("baidu_memory","1","spider_memory")
    send_metrics("douban_memory","1","spider_memory")
    send_metrics("douyin_memory","1","spider_memory")
    send_metrics("taobao_memory","1","spider_memory")
    send_metrics("xiaohongshu_memory","1","spider_memory")
    # registry = CollectorRegistry()
    # baidu_result = get_data("baidu")
    # if baidu_result:
    #     gauge_baidu = Gauge('spider_count', 'an example showed how to use gauge', ['job',"timetype"], registry=registry)
    #     gauge_baidu.labels("baidu",1).set(len(baidu_result))
    #     push_to_gateway("http://localhost:9091", job="baidu", registry=registry)

    # registry = CollectorRegistry()
    # douban_result = get_data("douban")
    # if douban_result:
    #     gauge_douban = Gauge('spider_count', 'an example showed how to use gauge', ['job',"timetype"], registry=registry)
    #     gauge_douban.labels("douban",1).set(len(douban_result))
    #     push_to_gateway("http://localhost:9091", job="douban", registry=registry)
    #
    # registry = CollectorRegistry()
    # douyin_result = get_data("douyin")
    # if douyin_result:
    #     gauge_douyin = Gauge('spider_count', 'an example showed how to use gauge', ['job',"timetype"], registry=registry)
    #     gauge_douyin.labels("douyin",1).set(len(douyin_result))
    #     push_to_gateway("http://localhost:9091", job="douyin", registry=registry)
    #
    # registry = CollectorRegistry()
    # taobao_result = get_data("taobao")
    # if taobao_result:
    #     gauge_taobao = Gauge('spider_count', 'an example showed how to use gauge', ['job',"timetype"], registry=registry)
    #     gauge_taobao.labels("taobao",1).set(len(taobao_result))
    #     push_to_gateway("http://localhost:9091", job="taobao", registry=registry)
    #
    # registry = CollectorRegistry()
    # xiaohongshu_result = get_data("xiaohongshu")
    # if xiaohongshu_result:
    #     gauge_xiaohongshu = Gauge('spider_count', 'an example showed how to use gauge', ['job',"timetype"], registry=registry)
    #     gauge_xiaohongshu.labels("xiaohongshu",1).set(len(xiaohongshu_result))
    #     push_to_gateway("http://localhost:9091", job="xiaohongshu", registry=registry)







    #return Response(generate_latest(registry), mimetype='text/plain')



if __name__ == '__main__':
    #req.request()
    while True:
        hello()
        print("指标发送成功")
        time.sleep(15)
    #app.run(host='0.0.0.0', port=5000)
