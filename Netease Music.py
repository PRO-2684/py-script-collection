from requests import get
from random import choice
path = r'E:\Music'
num = '0123456789'
heads = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'},
         {'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; HUAWEI NXT-TL00 Build/HUAWEINXT-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045008 Mobile Safari/537.36 V1_AND_SQ_8.2.0_1296_YYB_D QQ/8.2.0.4310 NetType/4G WebP/0.3.0 Pixel/1080 StatusBarHeight/66 SimpleUISwitch/1'})
down_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'

def download(url, path, head):
    print('Download from', url)
    try:
        t = get(url, headers=head)
        print('Got.')
    except:
        print('Fail. Please use F12 tools to download.')
    else:
        with open(path, 'wb') as f:
            print('Writing to ' + path)
            f.write(t.content)
def get_id(url):
    try:
        n = url.index('id=')
    except:
        print("Invalid/Don't support.")
        return False
    else:
        id = ''
        for i in url[n + 3:]:
            if i in num:
                id += i
            else:
                break
        return id


que_url = input('url:')
id = get_id(que_url)
if id:
    head = choice(heads)
    url = down_url.format(id)
    name = input('name: ')
    if name: id = name
    path += '\\' + id + '.mp3'
    download(url, path, head)

