#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import time

from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CollectorRegistry, Gauge, Histogram, Summary

app = Flask(__name__)
registry = CollectorRegistry()
counter = Counter('my_counter', 'an example showed how to use counter', ['machine_ip'], registry=registry)

gauge = Gauge('my_gauge', 'an example showed how to use gauge', ['machine_ip'], registry=registry)

buckets = (100, 200, 300, 500, 1000, 3000, 10000, float('inf'))
histogram = Histogram('my_histogram', 'an example showed how to use histogram', ['machine_ip'], registry=registry, buckets=buckets)
s = Summary('request_latency_seconds', 'Description of summary')



@app.route('/metrics')
def hello():
    counter.labels('spider1').inc(1)
    gauge.labels("spider2").set(176)
    histogram.labels('Histogram').observe(1001)
    s.observe(4.7)
    return Response(generate_latest(registry), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

