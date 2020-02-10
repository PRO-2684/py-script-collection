from requests import get
from time import time,localtime
from prettytable import PrettyTable as tb
def add_0(t):
    t=str(t)
    n=len(t)
    return '0'+t if n==1 else t
def cl(m,c):
    return(f'\033[{c};m{m}\033[0m')
ticks=time();print(cl('Now:',33))
now=localtime(ticks)
days='Mon','Tues','Wednes','Thurs','Fri','Satur','Sun'
y,m,d,h,mi,s,w=now[0:7]
m=add_0(m);d=add_0(d);h=add_0(h);s=add_0(s)
print(cl(f'{y}/{m}/{d}    {days[w]}day',33))
print(cl(f'{h}:{mi}:{s}',33))


loc='北京'#     地点
name='******'# 和风天气有的白嫖，自己去弄个来
key='********'# 快乐白嫖地址：https://dev.heweather.com/
# 注册完后将api的两项数据填入上面
api = 'https://free-api.heweather.net/s6/weather/forecast?' # API URL
data={'location':loc,
    'key':key
    }
response=get(api,params=data)
result=response.json()
result=result['HeWeather6'][0]['daily_forecast']
trans={'cond_txt_d':'白天天气',
        'cond_txt_n':'夜晚天气',
        'hum':'相对湿度',
        'mr':'月升时间',
        'ms':'月落时间',
        'pcpn':'降水量',
        'pop':'降水概率',
        'pres':'大气压',
        'sr':'日出时间',
        'ss':'日落时间',
        'tmp_max':cl('最高温度',31),
        'tmp_min':cl('最低温度',32),
        'uv_index':'紫外线强度',
        'vis':'能见度',
        'wind_deg':'风向角',
        'wind_dir':'风向',
        'wind_sc':'风力',
        'wind_spd':'风速'
        }
data=tb()
data.add_column('日期',[m for m in trans.values()])
for n in range(len(result)):
    tmp=result[n]
    data.add_column(tmp['date'],[tmp[m] for m in trans])
print(data)
