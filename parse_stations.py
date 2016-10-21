import re
import requests
from pprint import pprint

url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955"
r = requests.get(url, verify=False)
stations = re.findall(r"([\u4e00-\u9fa5]+)\|([A-Z]+)",r.text)
stations = dict(stations)
stations = dict(zip(stations.keys(),stations.values()))
pprint(stations,indent=4)
