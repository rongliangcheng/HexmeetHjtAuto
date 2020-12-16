import pytest
import allure
from time import sleep
from HJT_pkg.HjtWindowsSingleton import HjtWindowSingleton
from HJT_pkg.ContactPageObject import Contact

hjt_singleton = HjtWindowSingleton()
contact = Contact()



def setup_module():
    sleep(10)
    # hjt_singleton.start_hjt()


def teardown_module():
    hjt_singleton.close_hjt()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("通讯录")
@allure.feature("测试HJT APP的通讯录操作")
@allure.story("呼叫常用联系人")
def test_call_from_favorite():
    sleep(5)
    contact.call_from_favorite("RongliangVE210")


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("通讯录")
@allure.feature("测试HJT APP的通讯录操作")
@allure.story("从组织架构中查找联系人")
def test_call_from_organization():
    sleep(5)
    contact.call_from_organization("RongliangVE210")


# def test_close_hjt():
#     hjt_singleton.close_hjt()


if __name__ == '__main__':
    pytest.main(["-s", "test_contact.py"])
