import os
import sys

import allure
import pytest

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))))
from HJT_pkg.AppSettingPageObject import AppSetting
from HJT_pkg.ReserveMeetingPageObject import ReserveMeeting
from HJT_pkg.OperateInMeetingPageObject import OperateInMeeting
from HJT_pkg.joinAMeetingPageObject import JoinAMeeting
from HJT_pkg.HjtWindowsSingleton import HjtWindowSingleton
from time import sleep
import os
import shutil

login_user = "hjtautotest5"
remote_user = "RongliangVE210"
screenshot_dir = "H:\\Autotest\\"
reserve_meeting = ReserveMeeting()
operate_meeting = OperateInMeeting()
join_meeting = JoinAMeeting()
app_setting = AppSetting()
hjt_singleton = HjtWindowSingleton()

bandwidth_list = ["384K", "512K", "768K", "1M", "1.5M", "3M", "4M", "2M"]



def setup_module():
    hjt_singleton.start_hjt()


def teardown_module():
    hjt_singleton.close_hjt()


def __remove_screen_files():
    del_list = os.listdir(screenshot_dir)
    for f in del_list:
        file_path = os.path.join(screenshot_dir, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def __count_screen_files():
    file_list = os.listdir(screenshot_dir)
    print(file_list)
    return len(file_list)


def __join_and_quit_meeting():
    sleep(5)
    join_meeting.join_a_meeting_from_top_menu()
    sleep(10)
    operate_meeting.show_media_statistics()
    sleep(10)
    # operate_meeting.close_media_statistics()
    operate_meeting.hangup_call()


def __invite_self():
    reserve_meeting.reserve_meeting_from_panel()
    reserve_meeting.choose_now()
    reserve_meeting.choose_participants(login_user)
    reserve_meeting.now_meeting_confirm()
    sleep(20)
    operate_meeting.terminate_call()


def __join_and_share_whiteboard_then_exit():
    reserve_meeting.reserve_meeting_from_panel()
    reserve_meeting.choose_now()
    reserve_meeting.choose_participants(remote_user)
    reserve_meeting.now_meeting_confirm()
    sleep(5)
    reserve_meeting.join_now_meeting()
    sleep(5)
    operate_meeting.share_whiteboard()
    sleep(20)
    operate_meeting.stop_whiteboard()
    sleep(5)
    operate_meeting.terminate_call()


def __invite_others_and_join_the_meeting():
    reserve_meeting.reserve_meeting_from_panel()
    reserve_meeting.choose_now()
    reserve_meeting.choose_participants(remote_user)
    reserve_meeting.now_meeting_confirm()
    sleep(3)
    reserve_meeting.join_now_meeting()
    sleep(10)



@pytest.mark.flaky(rerun=1, reruns_delay=2)
@allure.feature("测试HJT APP的设置界面")
@allure.parent_suite("应用设置")
@allure.suite("创建遍历带宽会议并入会")
@allure.story("创建遍历带宽会议并入会")
def test_prepare_all():
    sleep(5)
    reserve_meeting.clear_reserved_meeting()
    sleep(5)
    __invite_others_and_join_the_meeting()
    operate_meeting.hangup_call()


@allure.feature("测试HJT APP的设置界面")
@allure.parent_suite("应用设置")
@allure.suite("改变带宽并入会")
@allure.story("改变带宽并入会")
@pytest.mark.parametrize('bandwidth', bandwidth_list)
def test_change_bandwidth(bandwidth):
    # for bandwidth in bandwidth_list:
    app_setting.chang_bandwidth(bandwidth)
    sleep(2)
    __join_and_quit_meeting()
    sleep(8)


@pytest.mark.flaky(rerun=1, reruns_delay=2)
@allure.feature("测试HJT APP的设置界面")
@allure.parent_suite("应用设置")
@allure.suite("结束带宽遍历会议")
@allure.story("结束带宽遍历会议")
def test_terminate_the_meeting():
    reserve_meeting.go_to_meeting_page()
    reserve_meeting.terminate_now_meeting()


@pytest.mark.flaky(rerun=1, reruns_delay=2)
@allure.feature("测试HJT APP的设置界面")
@allure.parent_suite("应用设置")
@allure.suite("改变语言")
@allure.story("改变语言")
def test_change_language():
    app_setting.chang_language("English")
    sleep(10)
    app_setting.chang_language("简体中文")


@pytest.mark.flaky(rerun=1, reruns_delay=2)
@allure.feature("测试HJT APP的设置界面")
@allure.parent_suite("应用设置")
@allure.suite("改变白板保持路径")
@allure.story("改变白板保持路径")
def test_change_screen_shot_path():
    app_setting.change_snapshot_path()


@pytest.mark.flaky(rerun=1, reruns_delay=2)
@allure.feature("测试HJT APP的设置界面")
@allure.parent_suite("应用设置")
@allure.suite("设置自动接听，并建会拉入")
@allure.story("设置自动接听，并建会拉入")
def test_change_auto_answer():
    app_setting.change_auto_answer()
    __invite_self()
    app_setting.change_auto_answer()


@pytest.mark.flaky(rerun=1, reruns_delay=2)
@allure.feature("测试HJT APP的设置界面")
@allure.parent_suite("应用设置")
@allure.suite("设置退出白板自动保存，并坚持文件")
@allure.story("设置退出白板自动保存，并坚持文件")
def test_auto_save_when_exit_whiteboard():
    __remove_screen_files()
    app_setting.change_auto_save_white_board_when_exit()
    __join_and_share_whiteboard_then_exit()
    app_setting.change_auto_save_white_board_when_exit()
    assert __count_screen_files()


@pytest.mark.flaky(rerun=1, reruns_delay=2)
@allure.feature("测试HJT APP的设置界面")
@allure.parent_suite("应用设置")
@allure.suite("设置自动隐藏姓名")
@allure.story("设置自动隐藏姓名")
def test_auto_hide_participant_site_name():
    app_setting.change_auto_hide_site_name()
    __invite_others_and_join_the_meeting()
    operate_meeting.hangup_call()
    reserve_meeting.terminate_now_meeting()
    app_setting.change_auto_hide_site_name()


@pytest.mark.flaky(rerun=1, reruns_delay=2)
@allure.feature("测试HJT APP的设置界面")
@allure.parent_suite("应用设置")
@allure.suite("设置入会后全屏模式")
@allure.story("设置入会后全屏模式")
def test_change_to_full_mode_meeting():
    app_setting.change_to_full_mode_meeting()
    __invite_others_and_join_the_meeting()
    operate_meeting.terminate_call_in_full_mode()
    app_setting.change_to_full_mode_meeting()


if __name__ == '__main__':
    pytest.main(["-s", "test_appsetting.py", "--alluredir=reports"])
