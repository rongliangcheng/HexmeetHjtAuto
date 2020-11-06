import pytest
import allure
import sys
import os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))))
from HJT_pkg.UnRegisterCallPageObject import UnRegisterCall
from HJT_pkg.HjtWindowsSingleton import HjtWindowSingleton
from HJT_pkg.ReserveMeetingPageObject import ReserveMeeting
from HJT_pkg.OperateInMeetingPageObject import OperateInMeeting
from time import sleep


unregister_call = UnRegisterCall()
hjt_singleton = HjtWindowSingleton()
reserve_meeting = ReserveMeeting()
operate_meeting = OperateInMeeting()
password = "000000000000"
server_addr = "cloudbeta.hexmeet.com"
conf_id = "13910001001"
conf_id_password = "12345"
show_name = "autotest"


def setup_module():
    hjt_singleton.start_hjt()


def teardown_module():
    hjt_singleton.close_hjt()


def __make_a_call(server_address, conference_id, display_name):
    unregister_call.fill_in_server_address(server_address)
    unregister_call.fill_in_conference_id(conference_id)
    unregister_call.fill_in_display_name(display_name)
    unregister_call.change_microphone_setting()
    unregister_call.change_camera_setting()
    unregister_call.change_microphone_setting()
    unregister_call.change_camera_setting()
    unregister_call.user_join_commit()


def __reserve_a_now_conference(password=""):
    sleep(1)
    reserve_meeting.go_to_meeting_page()
    sleep(1)
    reserve_meeting.reserve_meeting_from_panel()
    sleep(1)
    reserve_meeting.choose_now()
    if password != "":
        reserve_meeting.fill_password(password)
    reserve_meeting.now_meeting_confirm()
    reserve_meeting.join_now_meeting()
    sleep(10)
    operate_meeting.hangup_call()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("非注册呼入会议")
@allure.feature("测试HJT APP的未注册用户的入会操作")
@allure.story("匿名入会")
def test_normal_call():
    unregister_call.go_to_unregister_call_page()
    sleep(1)
    __make_a_call(server_addr, conf_id, show_name)
    sleep(1)
    unregister_call.fill_in_password(conf_id_password)
    sleep(30)
    operate_meeting.hangup_call()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("非注册呼入会议")
@allure.feature("测试HJT APP的未注册用户的入会操作")
@allure.story("创建带密码即时会议")
def test_reserve_a_now_password_conference():
    unregister_call.login_from_unregister_call_page()
    __reserve_a_now_conference(password)


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("非注册呼入会议")
@allure.feature("测试HJT APP的未注册用户的入会操作")
@allure.story("匿名入会并输入密码")
def test_unregister_call_password():
    unregister_call.go_to_unregister_call_page()
    sleep(1)
    unregister_call.user_join_commit()
    sleep(1)
    unregister_call.fill_in_password(password)
    sleep(30)
    operate_meeting.hangup_call()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("非注册呼入会议")
@allure.feature("测试HJT APP的未注册用户的入会操作")
@allure.story("匿名并同时输入会议号和密码")
def test_unregister_call_id_password_one_line():
    sleep(1)
    unregister_call.append_password("*" + password)
    sleep(1)
    unregister_call.user_join_commit()
    sleep(30)
    operate_meeting.hangup_call()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("非注册呼入会议")
@allure.feature("测试HJT APP的未注册用户的入会操作")
@allure.story("清除会议")
def test_terminate_reserve_call():
    unregister_call.login_from_unregister_call_page()
    reserve_meeting.terminate_now_meeting()


if __name__ == '__main__':
    pytest.main(["-s", "test_unregistercall.py"])
