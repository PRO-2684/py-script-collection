#用于实时查看肺炎动态
#请先安装requests, prettytable
from time import time
from json import loads
from requests import get
from prettytable import PrettyTable as tb
path='/storage/F655-DA70/python/temp/f.txt'
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_area_counts&callback=&_=%d'%int(time()*1000)
data = loads(get(url).json()['data'])
tb=tb()
tb.field_names=['国家','省','城市','确诊','疑似','治愈','死亡']
for i in data:
    tb.add_row([i['country'],i['area'],i['city'],i['confirm'],i['suspect'],i['heal'],i['dead']])
print(tb)
