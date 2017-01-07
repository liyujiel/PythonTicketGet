# coding: utf-8

import urllib3
urllib3.disable_warnings()
import re
import requests
from pprint import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971'

response = requests.get(url,verify = False)
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
pprint(dict(stations),indent=4)
