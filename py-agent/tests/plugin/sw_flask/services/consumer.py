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
import time

import requests

from skywalking import agent, config
from skywalking.decorators import runnable

if __name__ == '__main__':
    config.service_name = 'consumer-yf'
    config.logging_level = 'DEBUG'
    config.flask_collect_http_params = True
    config.collector_address = "127.0.0.1:11800"
    agent.start()

    from flask import Flask, jsonify

    app = Flask(__name__)

    @app.route("/users", methods=["POST", "GET"])
    def application():
        from skywalking.trace.context import get_context
        get_context().put_correlation("correlation", "correlation")

        @runnable(op="/users")
        def post():
            #while True:
            requests.post("http://127.0.0.1:9080/baidu")
            # requests.post("http://127.0.0.1:9081/douban")
            # requests.post("http://127.0.0.1:9082/douyin")
            # requests.post("http://127.0.0.1:9083/taobao")
            # requests.post("http://127.0.0.1:9084/xiaohongshu")
            #time.sleep(60)

        from threading import Thread
        t = Thread(target=post)
        t.start()

        t.join()

        return jsonify({"status":"okokokok"})


    @app.route("/users2", methods=["POST", "GET"])
    def application2():
        @runnable(op="/users2")
        def post():
            requests.post("http://127.0.0.1:9082/douyin")
            #time.sleep(60)
            #return jsonify({"status":"okokokok"})
        from threading import Thread
        t = Thread(target=post)
        t.start()
        t.join()
        return jsonify({"status": "okokokok"})
    PORT = 9087
    app.run(host='0.0.0.0', port=PORT, debug=True)
