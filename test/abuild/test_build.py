import subprocess
from time import sleep

import pytest
import sys
import os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))))
from HJT_pkg.AppVersion import AppVersion
from HJT_pkg.BuildVersion import BuildVersion
from HJT_pkg.HjtWindowsSingleton import HjtWindowSingleton
from HJT_pkg.Common import CommonClass
import re

projectName = "swep-evsdk-win-svc-qt-1.4.1"
hjt_singleton = HjtWindowSingleton()


def setup_module():
    hjt_singleton.start_hjt()


# def teardown_module():
#     hjt_singleton.close_hjt()


def test_install_build():
    appVersion = AppVersion()
    buildVersion = BuildVersion()

    current_version = appVersion.getAppVersion()
    build_version = buildVersion.last_build_version(projectName)

    if current_version.__contains__(str(build_version)):
        pass
    else:
        hjt_singleton.close_hjt()
        build_file_url = buildVersion.get_build_file_name(projectName, "exe")
        buildVersion.download_build(build_file_url, "HexmeetHJT.exe")
        buildVersion.install_build()
        sleep(60)
        matchObj = re.search(r'1\.4\.1\.([0-9]+)', build_file_url, re.I)

        CommonClass().createEnvironmentFile("allure-results/Environment.xml", matchObj.group())
        hjt_singleton.start_hjt()
        sleep(30)
        # 需要以创建新的appversion对象来获取新的app
        current_version = AppVersion().getAppVersion()

    assert current_version.__contains__(str(build_version))


if __name__ == '__main__':
    pytest.main(["-s", "test_build.py", "--alluredir=reports"])
