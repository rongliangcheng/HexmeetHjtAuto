import pytest
import allure
from time import sleep
import uiautomation as auto
from HJT_pkg.HjtWindowsSingleton import HjtWindowSingleton
from HJT_pkg.OperateInMeetingPageObject import OperateInMeeting
from HJT_pkg.ReserveMeetingPageObject import ReserveMeeting
from HJT_pkg.joinAMeetingPageObject import JoinAMeeting

hjt_singleton = HjtWindowSingleton()
reserve_meeting = ReserveMeeting()
join_a_meeting = JoinAMeeting()
remote_user = "RongliangVE210"
password = "1234"


@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
def setup_module():
    hjt_singleton.start_hjt()


def teardown_module():
    hjt_singleton.close_hjt()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
@allure.story("预约会议")
@allure.step("点击入会")
def test_click_reserve_meeting():
    sleep(3)
    reserve_meeting.clear_reserved_meeting()
    sleep(4)
    reserve_meeting.reserve_meeting_from_panel()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
@allure.story("预约会议")
@allure.step("点击入会")
def test_choose_date():
    sleep(2)
    reserve_meeting.choose_date()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
@allure.story("预约会议")
@allure.step("点击入会")
@allure.story("选择时间")
def test_choose_time():
    sleep(2)
    reserve_meeting.choose_time()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
@allure.story("预约会议")
@allure.step("选择时长")
def test_choose_duration():
    sleep(2)
    reserve_meeting.choose_duration()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
@allure.story("预约会议")
@allure.step("输入密码")
def test_fill_password():
    sleep(2)
    reserve_meeting.fill_password(password)


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
@allure.story("预约会议")
@allure.step("加入备注")
def test_fill_meeting_note():
    sleep(2)
    reserve_meeting.fill_meeting_notes("This is a reserved meeting")


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
@allure.story("预约会议")
@allure.step("选择与会者")
def test_choose_participant():
    sleep(2)
    reserve_meeting.choose_participants(remote_user)


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
@allure.story("预约会议")
@allure.step("随机会议号")
def test_use_random_number_as_meeting_room():
    auto.WheelDown(6)
    sleep(2)
    reserve_meeting.use_random_number_as_meeting_room()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
@allure.story("预约会议")
@allure.step("允许匿名入会")
def test_allow_anonymous():
    sleep(2)
    reserve_meeting.allow_anonymous_user()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
@allure.story("预约会议")
@allure.step("入会自动静音")
def test_mute_when_join_meeting():
    sleep(2)
    reserve_meeting.mute_when_join_meeting()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
@allure.story("预约会议")
@allure.step("创建会议")
def test_create_reserve_meeting():
    auto.WheelDown()
    sleep(2)
    reserve_meeting.reserve_confirm()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
@allure.story("预约会议")
@allure.step("对已经预约会议进行修改")
def test_edit_and_return_from_reserve_meeting():
    reserve_meeting.edit_reserve_meeting()
    sleep(2)
    reserve_meeting.return_from_edit_reserve()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
@allure.story("预约会议")
@allure.step("分享会议信息")
def test_share_and_return_from_reserve_meeting():
    reserve_meeting.share_reserve_meeting()
    sleep(2)
    reserve_meeting.return_from_share()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
@allure.story("预约会议")
@allure.step("删除预约会议")
def test_delete_reserve_meeting():
    reserve_meeting.delete_reserve_meeting()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
@allure.story("创建即时会议并入会")
def test_create_now_and_join():
    reserve_meeting.reserve_meeting_from_panel()
    sleep(1)
    reserve_meeting.choose_now()
    auto.WheelDown(7)
    reserve_meeting.now_meeting_confirm()
    sleep(1)
    reserve_meeting.control_now_meeting()
    sleep(1)
    reserve_meeting.invite_others_control_now_meeting(remote_user)
    sleep(1)
    reserve_meeting.join_now_meeting()
    operate_in_meeting = OperateInMeeting()
    operate_in_meeting.hangup_call()
    sleep(5)
    reserve_meeting.terminate_now_meeting()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.feature("测试HJT APP的设置预约会议操作")
@allure.story("创建带密码的即时会议然后加入")
def test_create_now_password_and_join():
    reserve_meeting.reserve_meeting_from_panel()
    sleep(1)
    reserve_meeting.choose_now()
    sleep(1)
    reserve_meeting.fill_password(password)
    auto.WheelDown(7)
    reserve_meeting.now_meeting_confirm()
    sleep(1)
    reserve_meeting.control_now_meeting()
    sleep(1)
    reserve_meeting.invite_others_control_now_meeting(remote_user)
    sleep(1)
    reserve_meeting.join_now_meeting()
    operate_in_meeting = OperateInMeeting()
    operate_in_meeting.hangup_call()
    sleep(5)
    join_a_meeting.join_a_meeting_from_panel_with_password(password)
    sleep(20)
    operate_in_meeting.hangup_call()
    sleep(5)
    join_a_meeting.join_a_meeting_from_panel_with_password_one_line(password)
    sleep(20)
    operate_in_meeting.hangup_call()
    sleep(5)
    reserve_meeting.terminate_now_meeting()


if __name__ == '__main__':
    pytest.main(["-s", "test_reservemeeting.py"])
