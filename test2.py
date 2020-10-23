import datetime

url = "http://172.17.2.64:8088/graphql"
d1 = datetime.datetime.now()
d3 = d1 - datetime.timedelta(days=10)
d1 = d1.split(" ")[0]
d3 = d1.split(" ")[0]
param = {"query":"query queryServiceTopo($duration: Duration!, $serviceIds: [ID!]!) {\n  topo: getServicesTopology(duration: $duration, serviceIds: $serviceIds) {\n    nodes {\n      id\n      name\n      type\n      isReal\n    }\n    calls {\n      id\n      source\n      detectPoints\n      target\n    }\n  }}","variables":{"duration":{"start":"2020-10-06","end":"2020-10-13","step":"DAY"},"serviceIds":["Y2xlYW5fcGxhdGZvcm0=.1","c3BpZGVyX2JhaWR1dGllYmE=.1","c3BpZGVyX211c2ljMTYz.1","c3BpZGVyX3BsYXRmb3Jt.1","cHJvdmlkZXI=.1"]}}
