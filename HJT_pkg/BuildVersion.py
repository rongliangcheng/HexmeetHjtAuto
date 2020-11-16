from time import sleep
import urllib.parse
from urllib.request import *
from http import cookiejar as cookielib

import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth



class BuildVersion:
    def __init__(self):
        self.buildUrl = "http://172.27.0.12:8080/view/HJT%20SVC%20EVSDK%20APP/job/swep-evsdk-win-svc-qt-1.4.0/"
        # self.session = requests.session()
        # self.session.cookies = cookielib.LWPCookieJar(filename="huihuCookies.txt")

    # def alogin(self):
    #     loginUrl = "http://172.27.0.12:8080/login?from=%2Fview%2FHJT%2520SVC%2520EVSDK%2520APP%2Fjob%2Fswep-evsdk-win-svc-qt-1.4.0%2F"
    #     userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
    #     header = {
    #         "Referer": loginUrl,
    #         'User-Agent': userAgent,
    #     }
    #     post_data = {
    #         "username": "chengrl",
    #         "password": "123456",
    #     }
    #
    #     res = self.session.post(loginUrl, data=post_data, headers=header)
    #     print(res.text)

    def login(self):
        username = "chengrl"
        password = "123456"

        auth = HTTPBasicAuth(username, password)
        loginUrl = "http://172.27.0.12:8080/login?from=%2Fview%2FHJT%2520SVC%2520EVSDK%2520APP%2Fjob%2Fswep-evsdk-win-svc-qt-1.4.0%2F"
        response = requests.post(loginUrl, auth=auth)
        print(response.text)

    def getBuildVersion(self):
        try:
            page = self.session.get(self.buildUrl)
            if page.status_code == 200:
                print(page.text)
        except requests.RequestException:
            return None


if __name__ == '__main__':
    BuildVersion().login()
