import pytest
import allure
from time import sleep
from HJT_pkg.HjtWindowsSingleton import HjtWindowSingleton
from HJT_pkg.joinAMeetingPageObject import JoinAMeeting
from HJT_pkg.OperateInMeetingPageObject import OperateInMeeting

hjt_singleton = HjtWindowSingleton()
join_meeting_po = JoinAMeeting()
operate_in_meeting = OperateInMeeting()


def setup_module():
    hjt_singleton.start_hjt()


def teardown_module():
    hjt_singleton.close_hjt()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("从菜单栏呼叫")
@allure.step("入会")
def test_joinameetingfromtopmenu():
    sleep(3)
    join_meeting_po.join_a_meeting_from_top_menu()
    assert join_meeting_po.is_in_meeting()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("会中操作")
@allure.step("静音及静音解除")
def test_mute_umute_audio():
    operate_in_meeting.umte_umute_audio()
    sleep(10)
    operate_in_meeting.umte_umute_audio()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("会中操作")
@allure.step("关掉摄像头然后打开")
def test_mute_umute_camera():
    operate_in_meeting.mute_umute_camera()
    sleep(10)
    operate_in_meeting.mute_umute_camera()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("会中操作")
@allure.step("共享桌面")
def test_share_content():
    operate_in_meeting.show_media_statistics()
    operate_in_meeting.share_content()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("会中操作")
@allure.step("共享桌面 1080P 及发送声音")
def test_share_content_sound_1080P():
    operate_in_meeting.share_content_sound_highframerate()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("会中操作")
@allure.step("共享白板")
def test_share_white_board():
    operate_in_meeting.share_whiteboard()
    operate_in_meeting.close_media_statistics()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("会中操作")
@allure.step("切换分屏")
def test_switch_video_layout():
    operate_in_meeting.switch_video_layout()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("会中操作")
@allure.step("改名")
def test_change_name():
    operate_in_meeting.rename("AAAAbbbb")
    sleep(10)
    operate_in_meeting.rename_enter_key("ccccDDDD{ENTER}")


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("会中操作")
@allure.step("只有音频")
def test_audio_only():
    operate_in_meeting.audio_only()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("会中操作")
@allure.step("音频升级音视频")
def test_av_escalation():
    operate_in_meeting.av_escalation()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("会中操作")
@allure.step("调节音量")
def test_tune_volume():
    operate_in_meeting.change_volume()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("会中操作")
@allure.step("最小化本地视频")
def test_minimise_local_video():
    operate_in_meeting.minimise_local_video()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("会中操作")
@allure.step("恢复本地视频")
def test_maximise_local_video():
    operate_in_meeting.maximise_local_vidoe()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("会中操作")
@allure.step("挂断会议")
def test_hangup():
    operate_in_meeting.hangup_call()
    # assert not join_meeting_po.isInMeeting()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("从桌面呼叫入会")
@allure.step("从桌面呼叫入会")
def test_join_meeting_from_panel():
    join_meeting_po.join_a_meeting_from_panel()
    assert join_meeting_po.is_in_meeting()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("从桌面呼叫入会")
@allure.step("挂断会议")
def test_hangup_2():
    operate_in_meeting.hangup_call()
    # assert not join_meeting_po.isInMeeting()


# def test_close_hjt():
#     hjt_singleton.close_hjt()


if __name__ == '__main__':
    pytest.main(["-s", "test_operatemeeting.py"])
