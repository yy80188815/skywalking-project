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

from skywalking import config, agent

from mysql_connect import MysqlTaskConfig

if __name__ == '__main__':
    config.service_name = 'spider-cleansing'
    config.logging_level = 'INFO'
    config.collector_address = "172.17.2.64:11800"
    agent.start()

    topic = "skywalking"
    server_list = ["127.0.0.1:9092"]
    group_id = "skywalking"
    client_id = "0"

    from kafka import KafkaConsumer
    from kafka import TopicPartition
    consumer = KafkaConsumer(group_id=group_id,
                             client_id=client_id,
                             bootstrap_servers=server_list)
    partition = TopicPartition(topic, int(client_id))
    consumer.assign([partition])
    mysqldb = MysqlTaskConfig().get_instance()
    for msg in consumer:
        print(msg)
        mysqldb.mysql_data_write([["cleansing", "test", int(time.time())]])

