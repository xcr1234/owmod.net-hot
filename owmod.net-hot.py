from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import requests
import random
import time

'''
owmod.net hot script
author: misaka#51577 
https://github.com/xcr1234/owmod.net-hot


env:
pip install selenium
pip install beautifulsoup4
'''


proxys = []


for i in range(1,10):
    print("try get http proxy info,page:%d" % i)
    res = requests.get(url='http://www.89ip.cn/index_%d.html' % i)
    res.encoding='utf-8'
    soup = BeautifulSoup(res.text, "html.parser")
    trs = soup.find('table').find('tbody').find_all('tr')
    for tr in trs:
        td = tr.find_all('td')
        proxys.append((td[0].text.strip(),(int)(td[1].text.strip()),td[2].text.strip()))


print(proxys)
succ_count = 0

for i in range(len(proxys)):
    proxy = proxys[i]
    print("try to use proxy %s:%d %s" % (proxy[0],proxy[1],proxy[2]))
    print("proxy %d/%d" % (i+1,len(proxys)))
    ops = Options()
    ops.add_argument("--proxy-server=http://%s:%d" % (proxy[0],proxy[1]))
    browser=webdriver.Chrome(chrome_options = ops)
    try:
        browser.delete_all_cookies()
        browser.get('https://www.owmod.net/work/view/15')
        sc = browser.find_element_by_class_name('share-code')
        wait=random.uniform(2,6)
        print("wait %d"%wait)
        time.sleep(wait)
        ac=sc.find_element_by_class_name('ant-card-body')
        print(ac.text)
        print("move & click..")
        ActionChains(browser).move_to_element(ac).click(ac).perform()
        # wait click operation to finish
        time.sleep(5)
        succ_count = succ_count + 1
        print("success count: %d" % succ_count)
    except Exception as e:
        # if proxy is invalid `browser.find_element_by_class_name` will throw the exception:
        # no such element: Unable to locate element: {"method":"class name","selector":"share-code"}
        print("error",e)
    finally:
        print("quit browser")
        browser.quit()

