#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import time

from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CollectorRegistry, Gauge, Histogram, push_to_gateway

app = Flask(__name__)
registry = CollectorRegistry()
counter = Counter('my_counter', 'an example showed how to use counter', ['machine_ip'], registry=registry)

gauge = Gauge('my_gauge', 'an example showed how to use gauge', ['machine_ip',"instance"], registry=registry)
gauge2 = Gauge('node_cpu_seconds_total', 'an example showed how to use gauge', ['cpu'], registry=registry)

buckets = (100, 200, 300, 500, 1000, 3000, 10000, float('inf'))
histogram = Histogram('my_histogram', 'an example showed how to use histogram', ['machine_ip'], registry=registry, buckets=buckets)

#@app.route('/metrics')
def hello():

    registry = CollectorRegistry()
    sql = "select * from f_spider_data_test where f_servername='baidu'"

    gauge = Gauge('my_gauge', 'an example showed how to use gauge', ['machine_ip', "instance"], registry=registry)
    gauge2 = Gauge('node_cpu_seconds_total', 'an example showed how to use gauge', ['cpu'], registry=registry)


    counter.labels('spider1').inc(1)
    gauge.labels("spider2","consumer-yf").set(random.randint(50,100))
    gauge2.labels("0")
    histogram.labels('Histogram').observe(1001)
    push_to_gateway("localhosr:9091", job="python-spider", registry=registry)
    return Response(generate_latest(registry), mimetype='text/plain')



if __name__ == '__main__':
    #req.request()
    while True:
        time.sleep(15)
        counter.labels('spider1').inc(1)
        gauge.labels("spider2").set(176)
        gauge2.labels("0")
        histogram.labels('Histogram').observe(1001)
        push_to_gateway("localhost:9091", job="python-spider-2", registry=registry)
        print("指标发送成功")
    #app.run(host='0.0.0.0', port=5000)
