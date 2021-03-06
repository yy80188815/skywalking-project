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
from mysql_connect import MysqlTaskConfig

from skywalking import agent, config
from skywalking.decorators import runnable
from spider import spider

if __name__ == '__main__':
    config.service_name = 'srv-data'
    config.logging_level = 'DEBUG'
    config.flask_collect_http_params = True
    config.collector_address = "172.17.2.64:11800"
    agent.start()

    from flask import Flask, jsonify

    app = Flask(__name__)


    @app.route("/data", methods=["POST", "GET"])
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
        mysqldb.mysql_data_read("select * from f_spider_data_test where f_created_at > 1603086113")

        return jsonify({"status":"okokokok"})

    PORT = 9085
    app.run(host='0.0.0.0', port=PORT, debug=True)
