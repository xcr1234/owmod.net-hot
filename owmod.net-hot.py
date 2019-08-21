import requests
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'referer':'https://www.owmod.net/work/view/15'}
for i in range(1,10):
    res = requests.get(url="https://www.owmod.net/api/stat/copy?id=15", headers=headers)
    res.encoding='utf-8'
    print(res.text)
