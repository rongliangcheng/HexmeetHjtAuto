import pytest
import allure
from time import sleep
from HJT_pkg.HjtWindowsSingleton import HjtWindowSingleton
from HJT_pkg.joinAMeetingPageObject import JoinAMeeting
from HJT_pkg.OperateInMeetingPageObject import OperateInMeeting
from HJT_pkg.Screen import CaptureScreen
from PIL import Image
from PIL import ImageChops

hjt_singleton = HjtWindowSingleton()
join_meeting_po = JoinAMeeting()
operate_in_meeting = OperateInMeeting()
fullscreenbox = (0, 0, 2560, 1440)


def setup_module():
    hjt_singleton.start_hjt()


def teardown_module():
    hjt_singleton.close_hjt()


def capture_attach_pic(pic_name, description, _bbox=(645, 316, 1918, 1072)):
    CaptureScreen.capture_attach_pic("../pics/" + pic_name, description, _bbox)


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.suite("从菜单栏呼叫入会")
@allure.story("从菜单栏呼叫入会")
@allure.step("入会")
def test_joinameetingfromtopmenu():
    sleep(5)
    join_meeting_po.join_a_meeting_from_top_menu()
    # capture_attach_pic("joinameetingfromtopmenu.png", "joinameetingfromtopmenu")
    assert join_meeting_po.is_in_meeting()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("静音及静音解除")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("静音及静音解除")
@allure.step("静音及静音解除")
def test_mute_umute_audio():
    operate_in_meeting.umte_umute_audio()
    sleep(10)
    capture_attach_pic("umte_umute_audio1.png", "umte_umute_audio")
    operate_in_meeting.umte_umute_audio()
    capture_attach_pic("umte_umute_audio2.png", "umte_umute_audio")


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("关掉摄像头然后打开")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("关掉摄像头然后打开")
@allure.step("关掉摄像头然后打开")
def test_mute_umute_camera():
    operate_in_meeting.mute_umute_camera()
    sleep(10)
    capture_attach_pic("mute_umute_camera1.png", "mute_umute_camera")
    operate_in_meeting.mute_umute_camera()
    capture_attach_pic("mute_umute_camera2.png", "mute_umute_camera")


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("共享桌面")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("共享桌面")
@allure.step("共享桌面")
def test_share_content():
    operate_in_meeting.show_media_statistics()
    operate_in_meeting.share_content()
    capture_attach_pic("share_content.png", "share_content", fullscreenbox)


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("共享桌面 1080P 及发送声音")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("共享桌面 1080P 及发送声音")
@allure.step("共享桌面 1080P 及发送声音")
def test_share_content_sound_1080P():
    operate_in_meeting.share_content_sound_highframerate()
    capture_attach_pic("share_content_sound_highframerate.png", "share_content_sound_highframerate", fullscreenbox)


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("共享白板")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("共享白板")
@allure.step("共享白板")
def test_share_white_board():
    operate_in_meeting.share_whiteboard()
    capture_attach_pic("share_whiteboard.png", "share_whiteboard")
    operate_in_meeting.close_media_statistics()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("切换分屏")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("切换分屏")
@allure.step("切换分屏")
def test_switch_video_layout():
    operate_in_meeting.switch_video_layout()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("改名")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("改名")
@allure.step("改名")
def test_change_name():
    operate_in_meeting.rename("AAAAbbbb")
    sleep(10)
    operate_in_meeting.rename_enter_key("ccccDDDD{ENTER}")
    capture_attach_pic("rename.png", "rename")


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("只有音频")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("只有音频")
@allure.step("只有音频")
def test_audio_only():
    operate_in_meeting.audio_only()
    capture_attach_pic("audio_only.png", "audio_only")


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("音频升级音视频")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("音频升级音视频")
@allure.step("音频升级音视频")
def test_av_escalation():
    try:
        operate_in_meeting.av_escalation()
    except TimeoutError as e:
        print(e)
        operate_in_meeting.close_media_statistics()
        operate_in_meeting.av_escalation()

    capture_attach_pic("av_escalation.png", "av_escalation")


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("调节音量")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("调节音量")
@allure.step("调节音量")
def test_tune_volume():
    operate_in_meeting.change_volume()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("最小化本地视频")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("最小化本地视频")
@allure.step("最小化本地视频")
def test_minimise_local_video():
    operate_in_meeting.minimise_local_video()
    capture_attach_pic("minimise_local_video.png", "minimise_local_video")


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("恢复本地视频")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("恢复本地视频")
@allure.step("恢复本地视频")
def test_maximise_local_video():
    operate_in_meeting.maximise_local_video()
    capture_attach_pic("maximise_local_video.png", "maximise_local_video")


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("最大化窗口")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("最大化窗口")
@allure.step("最大化窗口")
def test_maximise_windows():
    operate_in_meeting.maximise_window()
    capture_attach_pic("maximise_local_video.png", "maximise_local_video", fullscreenbox)


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("恢复窗口")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("恢复窗口")
@allure.step("恢复窗口")
def test_restore_window_from_max():
    operate_in_meeting.restore_window_from_maximise()
    capture_attach_pic("restore_window_from_maximise.png", "restore_window_from_maximise")


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("全屏视频")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("全屏视频")
@allure.step("全屏视频")
def test_video_fullscreen():
    operate_in_meeting.video_fullscreen()
    capture_attach_pic("video_fullscreen.png", "video_fullscreen", fullscreenbox)


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("从全屏恢复视频")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("从全屏恢复视频")
@allure.step("从全屏恢复视频")
def test_restore_from_fullscreen():
    operate_in_meeting.video_restore_from_fullscreen()
    capture_attach_pic("video_restore_from_fullscreen.png", "video_restore_from_fullscreen")


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("挂断会议")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("挂断会议")
@allure.step("挂断会议")
def test_hangup():
    operate_in_meeting.hangup_call()
    # assert not join_meeting_po.isInMeeting()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("从桌面呼叫入会，静音，关摄像头呼叫入会并且挂断")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("从桌面呼叫入会，静音，关摄像头呼叫入会并且挂断")
@allure.step("从桌面静音，关摄像头呼叫入会并且挂断")
def test_join_meeting_from_panel_mute():
    join_meeting_po.join_a_meeting_from_panel("true")
    sleep(10)
    # capture_attach_pic("join_a_meeting_from_panel_mute.png", "join_a_meeting_from_panel_mute", (645, 357, 1915, 1068))
    operate_in_meeting.hangup_call()
    # assert ImageChops.difference(Image.open("../pics/join_a_meeting_from_panel_mute.png"), Image.open("../Pictures/join_a_meeting_from_panel_mute.png")).getbbox() is None


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("会议控制")
@allure.suite("从桌面呼叫入会并挂断")
@allure.feature("测试HJT APP的会议中控制操作")
@allure.story("从桌面呼叫入会并挂断")
@allure.step("从桌面呼叫入会并挂断")
def test_join_meeting_from_panel():
    join_meeting_po.join_a_meeting_from_panel()
    capture_attach_pic("join_a_meeting_from_panel.png", "join_a_meeting_from_panel")
    assert join_meeting_po.is_in_meeting()
    sleep(10)
    operate_in_meeting.hangup_call()
    # assert not join_meeting_po.isInMeeting()


if __name__ == '__main__':
    pytest.main(["-s", "test_operatemeeting.py"])
