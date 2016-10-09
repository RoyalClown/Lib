import gzip
import json

import requests
from bs4 import BeautifulSoup

from Connection.Proxy import Proxy
from Constant.Connection import *


class HtmlAnalyse:
    def __init__(self, url, is_proxy=False, is_cookie=False):
        self.url = url
        self._session = requests.Session()
        self._session.headers.update(Default_Header)
        if is_proxy:
            proxy = Proxy()
            proxy_ip = proxy.validate_ip()
            self._session.proxies.update(proxy_ip)
        if is_cookie:
            with open("I:\\PythonPrj\\zhihu\\test.json") as f:
                cookies = f.read()
            print(cookies)
            cookies_dict = json.loads(cookies)
            self._session.cookies.update(cookies_dict)

    # 获得页面内容
    def get_contents(self):
        contents = self._session.get(self.url).text
        return contents

    # 获得bs对象
    def get_bs_contents(self):
        bs_contents = BeautifulSoup(self.get_contents(), "html.parser")
        return bs_contents

    # 解压文本
    def explode(self):
        content = self.get_contents()
        try:  # 尝试解压
            print('正在解压.....')

            content = gzip.decompress(content)
            print('解压完毕!')
        except:
            print('未经压缩, 无需解压')
        return content


if __name__ == "__main__":
    html_analyse = HtmlAnalyse("http://www.baidu.com")
    content = html_analyse.get_bs_contents()
    print(content)
