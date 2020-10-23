#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import requests
from mysql_connect import MysqlTaskConfig

from skywalking import agent, config
from skywalking.decorators import runnable
from spider import spider

if __name__ == '__main__':
    config.service_name = 'baidu.com'
    config.logging_level = 'DEBUG'
    config.flask_collect_http_params = True
    config.collector_address = "172.17.2.64:11800"
    agent.start()

    from flask import Flask, jsonify

    app = Flask(__name__)

    @app.route("/baidu", methods=["POST", "GET"])
    def application():
        from skywalking.trace.context import get_context
        get_context().put_correlation("correlation", "correlation")
        # @runnable(op="/test")
        # def post():
        #     requests.post("http://127.0.0.1:9092/users")
        #
        # from threading import Thread
        # t = Thread(target=post)
        # t.start()
        #
        # res = requests.post("http://127.0.0.1:9092/users")
        #
        # t.join()
        mysqldb = MysqlTaskConfig().get_instance()
        spider(65, 66, mysqldb, "baidu")
        requests.get("http://127.0.0.1:9081/douban1")
        from kafka import KafkaProducer
        producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], api_version=(1, 0, 1))
        producer.send('skywalking', b'baidu')
        return jsonify({"status":"okokokok"})


    @app.route("/baidu1", methods=["POST", "GET"])
    def application1():
        return jsonify({"status":"okokokok"})
    PORT = 9080
    app.run(host='0.0.0.0', port=PORT, debug=True)
