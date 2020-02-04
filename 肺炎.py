from requests import get
from time import localtime
from prettytable import PrettyTable
def add_0(n):
    if n: return str(n)
    else: return '0'
def color(m):
    return(f'\033[33;m{m}\033[0m')
def time(tick):
    days='Mon','Tues','Wednes','Thurs','Fri','Satur','Sun'
    y,m,d,h,mi,s,w=localtime(tick)[0:7]
    return color(f'{y}/{m}/{d} {days[w]}day {h}:{mi}:{s}')
data = get('https://service-f9fjwngp-1252021671.bj.apigw.tencentcs.com/release/pneumonia').json()['data']
print('国内更新时间:', time(data['statistics']['modifyTime']/1000))
wanted = ['confirmed', 'cured', 'dead']
provinces = set()

#国内
tb = PrettyTable()
tb.field_names = ["省份", "确诊", "治愈", "死亡"]
for province in data['listByArea']:
    provinces.add(province['provinceShortName'])
    tb.add_row([province['provinceShortName']]+[add_0(province[attr]) for attr in wanted])
tb.add_row([color('总计')]+[color(add_0(data['statistics'][attr+'Count'])) for attr in wanted])
tb.add_row([color('增量')]+[color(add_0(data['statistics'][attr+'Incr'])) for attr in wanted])
print(tb)
while True:
    q = input('详细信息:(xx省份/外国)')
    if q == '外国':
        #外国
        tb = PrettyTable()
        tb.field_names = ["国家", "确诊", "治愈", "死亡"]
        for country in data['listByOther']:
            tb.add_row([country['name']]+[add_0(country[attr]) for attr in wanted])
        print(tb)
    elif q in provinces:
        #城市
        tb = PrettyTable()
        tb.field_names = ["城市", "确诊", "治愈", "死亡"]
        for province in data['listByArea']:
            if province['provinceShortName'] == q: areas = province['cities']; break
        for area in areas:
            tb.add_row([area[attr] for attr in ['cityName']+wanted])
        tb.add_row([color(q)]+[color(add_0(area[attr])) for attr in wanted])
        print(tb)
    else: break
