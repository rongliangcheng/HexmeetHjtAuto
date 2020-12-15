import jenkins
import requests
import os
import time
import logging
from requests.auth import HTTPBasicAuth

class BuildVersion:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.buildUrl = "http://172.27.0.12:8080/login?from=%2Fview%2FHJT%2520SVC%2520EVSDK%2520APP%2Fjob%2Fswep-evsdk-win-svc-qt-1.4.1%2FlastSuccessfulBuild%2Fartifact%2F"
        self.server = jenkins.Jenkins(self.buildUrl, username="chengrl", password="123456")

    def last_build_version(self, projectName):
        self.log.debug("last_build_version")
        projectJobs = self.server.get_all_jobs()
        for job in projectJobs:
            if job['fullname'] == projectName:
                info = self.server.get_job_info(projectName)
                return info['lastSuccessfulBuild']['number']
        return None

    def get_build_file_name(self, projectName, fileNameRegi):
        self.log.debug("get_build_file_name")
        build_base_url = "http://172.27.0.12:8080/view/HJT%20SVC%20EVSDK%20APP/job/swep-evsdk-win-svc-qt-1.4.1/lastSuccessfulBuild/"
        build_info = self.server.get_build_info(projectName, self.last_build_version(projectName))
        build_url = ""
        for artifact in build_info['artifacts']:
            if( fileNameRegi in artifact['fileName']):
                build_url = build_base_url + 'artifact/' + artifact['relativePath']
        return build_url

    def download_build(self, fileurl, target):
        self.log.debug("download_build")
        s = requests.session()
        fileContent = s.get(fileurl, auth=('chengrl', '123456'))
        with open(target, 'wb') as content:
             content.write(fileContent.content)

    def install_build(self):
        self.log.debug("install_build")
        install_command = "cmd.exe /c  HexmeetHJT.exe /s /v/qn"
        del_command = "cmd.exe /c del HexmeetHJT.exe "
        os.system(install_command)
        time.sleep(60)
        os.system(del_command)
        self.log.debug("finished")


if __name__ == '__main__':
    projectName = "swep-evsdk-win-svc-qt-1.4.1"
    build_version = BuildVersion()
    build_file_url = build_version.get_build_file_name(projectName, "exe")
    build_version.download_build(build_file_url, "HexmeetHJT.exe")
    build_version.install_build()
    # os.system("cmd.exe /c  HexmeetHJT.exe /s /v/q")
