#!/usr/bin/env python
#encoding: utf-8
import json
import os
import requests

city = '珠海'
key = '0b60a581d55a43a5803413912101f276'

get_location = requests.get('https://geoapi.heweather.net/v2/city/lookup?location={city}&key={key}'.format(city=city,key=key))

location = get_location.json()['location'][0]['id']
# 上面获取城市location 知道可写死，减少请求

resp = requests.get('https://devapi.heweather.net/v7/weather/now?location={location}&key={key}'.format(location=location,key=key))

wether = resp.json()['now']

outstr = '珠海今天天气 {} ,温度 {} ,风向 {} ,风力{}级 ,相对湿度 {} ,降水量{}'.format(wether['text'], wether['temp'], wether['windDir'],wether['windScale'],  wether['humidity'],wether['precip'])
print(outstr)
cmd = 'ilang "' + outstr + '"'
os.system(cmd)