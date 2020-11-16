import pytest
import allure
from HJT_pkg.LoginPageObject import UserLogin
from HJT_pkg.HjtWindowsSingleton import HjtWindowSingleton
from time import sleep

user_login = UserLogin()
hjt_singleton = HjtWindowSingleton()



def setup_module():
    hjt_singleton.start_hjt()


def teardown_module():
    hjt_singleton.close_hjt()


def __user_login(server_addr, account, password):
    user_login.fill_in_server_address(server_addr)
    user_login.fill_in_account(account)
    user_login.fill_in_password(password)
    user_login.user_login_commit()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("登录")
@allure.feature("测试HJT APP的登录界面的操作")
@allure.story("回到登录界面")
def test_go_to_login_page():
    sleep(3)
    user_login.go_to_login_page()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("登录")
@allure.feature("测试HJT APP的登录界面的操作")
@allure.story("以错误账号登陆")
def test_login_with_wrong_account():
    __user_login("cloudbeta.hexmeet.com", "hjtautotes", "123456")
    user_login.login_fail_commit()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("登录")
@allure.feature("测试HJT APP的登录界面的操作")
@allure.story("登录不正确的服务器")
def test_login_with_wrong_server_address():
    __user_login("loudbeta.hexmeet.com", "hjtautotest5", "123456")
    user_login.login_fail_commit()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("登录")
@allure.feature("测试HJT APP的登录界面的操作")
@allure.story("尝试5遍被锁5分钟")
def test_login_with_5_times_wrong_password():
    for i in range(6):
        __user_login("cloudbeta.hexmeet.com", "hjtautotest5", "12346")
        sleep(1)
        user_login.login_fail_commit()
        sleep(10)


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("登录")
@allure.feature("测试HJT APP的登录界面的操作")
@allure.story("正常登录成功")
def test_login_with_normal():
    sleep(300)
    __user_login("cloudbeta.hexmeet.com", "hjtautotest5", "123456")


#
# def test_close_hjt():
#     hjt_singleton.close_hjt()


if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])
