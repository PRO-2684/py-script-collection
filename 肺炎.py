from requests import get
from bs4 import BeautifulSoup as bs
from json import loads
from prettytable import PrettyTable
#from os import system# win10
#system('')# win10
def add_0(n):
    if n: return str(n)
    else: return '0'
def pr(s):
    global i
    n = i[s]
    if n: return int(n)
    else: return 0
def cl(m):
    return(f'\033[33;m{m}\033[0m')
head = {'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; HUAWEI NXT-TL00 Build/HUAWEINXT-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.58 Mobile Safari/537.36 MMWEBID/5671 MicroMessenger/7.0.10.1580(0x27000AF1) Process/tools NetType/WIFI Language/zh_CN ABI/arm64'}
response = get('https://voice.baidu.com/act/newpneumonia/newpneumonia', headers=head)
soup = bs(response.text, features="html.parser")
res = soup.findAll('script')
d = 'V.conf'
for i in res:
    s = i.text
    if d in s:
        m = s.index('V.conf')+9
        n = s.index('caseOutsideList')
        data = loads(s[m:n - 2] + '}]}')['component'][0]
        break
print('更新时间:', data['mapLastUpdatedTime'])
b = c = d = 0; detail = {}
tb = PrettyTable()
tb.field_names = ["省份", "确诊", "治愈", "死亡"]
tb.align = "l"
for i in data['caseList'][::-1]:
    x=pr('confirmed'); y=pr('crued'); z=pr('died')
    tb.add_row([i['area'], x, y, z])
    detail[i['area']] = [i['subList'], add_0(x), add_0(y), add_0(z)]
    b += x; c += y; d += z
tb.add_row([cl(i) for i in ['总计', b, c, d]])
# i:{'confirmed': '1', 'died': '', 'crued': '', 'area': '西藏', 'subList': [{'city': '拉萨', 'confirmed': '1', 'died': '', 'crued': ''}]}
print(tb)
while True:
    q = input('详细信息: ')
    if q in detail:
        tb = PrettyTable()
        tb.field_names = ["地区", "确诊", "治愈", "死亡"]
        tb.align = "l"
        m = detail[q]
        tb.add_row([cl(m) for m in [q, m[1], m[2], m[3]]])
        for i in m[0]:# i为对应的subList中的每一项
            tb.add_row([i['city'], add_0(i['confirmed']), add_0(i['crued']), add_0(i['died'])])
        print(tb)
    else:break
a = input('Finished.')
