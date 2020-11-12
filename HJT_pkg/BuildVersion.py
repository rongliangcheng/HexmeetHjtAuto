from time import sleep
import requests


class BuildVersion:
    def __init__(self):
        self.buildUrl = "http://172.27.0.12:8080/view/HJT%20SVC%20EVSDK%20APP/job/swep-evsdk-win-svc-qt-1.4.0/"
        self.loginUrl = "http://172.27.0.12:8080/login?from=%2Fview%2FHJT%2520SVC%2520EVSDK%2520APP%2Fjob%2Fswep-evsdk-win-svc-qt-1.4.0%2F"
        self.session = requests.session()

        data = [
            ('opr', 'pwdLogin'),
            ('userName', 'chengrl'),
            ('pwd', '123456'),
            ('rememberPwd', '0'),
        ]

        sleep(5)
        res = self.session.post(self.loginUrl, data)
        print(res)

    def getBuildVersion(self):
        try:
            page = self.session.get(self.buildUrl)
            if page.status_code == 200:
                print(page.text)
        except requests.RequestException:
            return None


if __name__ == '__main__':
    BuildVersion().getBuildVersion()
