import uiautomation as auto
import time


class OperateInMeeting:

    def __init__(self):
        self.hjtMeetingWindow = auto.WindowControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg")
        self.meetingWindowControl = self.hjtMeetingWindow.GroupControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.m_pWgtTitleBar")
        self.meetingLabel = self.hjtMeetingWindow.GroupControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.m_pWgtTitleBar").TextControl(searchDepth=1, ClassName="QLabel")
        self.meetingControlToolBar = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutBackgroundDlg") \
            .WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutCoverDlg").WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutToolbarDlg")

    def show_media_statistics(self):
        self.hjtMeetingWindow.GroupControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.m_pWgtTitleBar")\
            .ButtonControl(searchDepth=2, AutomationId="CLayoutBackgroundDlg.m_pWgtTitleBar.m_pLeftWidget.m_pBtnNetworkQuality").Click()
        # 点击完后，把鼠标移到视频，以便移到鼠标调出工具条
        x, y = auto.GetCursorPos()
        auto.Click(x, y+40)

    def close_media_statistics(self):
        auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CMediaStatisticsDlg")\
            .ButtonControl(searchDepth=2, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.CMediaStatisticsDlg.m_pWgtTitleBar.m_pBtnClose").Click()

    def umte_umute_audio(self):
        """解除静音"""
        time.sleep(10)
        self.meetingLabel.Click()
        self.meetingControlToolBar.CheckBoxControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnEnableMic").Click()

    def mute_umute_camera(self):
        """停止视频"""
        time.sleep(10)
        self.meetingLabel.Click()
        self.meetingControlToolBar.CheckBoxControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnEnableCamera").Click()

    def share_content(self):
        """分享屏幕 共享声音 流畅度优先"""
        shareContentWindow = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutBackgroundDlg").WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutCoverDlg") \
            .WindowControl(searchDepth=1, ClassName="ev_app::views::CSelectShareContent")
        contentInSharingWindow = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CbackgroundWidget")

        time.sleep(10)
        self.meetingLabel.Click()
        self.meetingControlToolBar.ButtonControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnShare").Click()
        shareContentWindow.CheckBoxControl(searchDepth=2, Name="共享电脑声音").Click()
        shareContentWindow.CheckBoxControl(searchDepth=2, Name="流畅度优先").Click()
        time.sleep(2)
        shareContentWindow.ButtonControl(searchDepth=2, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CSelectShareContent.toolbar.pBtShare").Click()
        time.sleep(30)
        contentInSharingWindow.TextControl(searchDepth=7, Name="停止分享").Click()
        time.sleep(2)
        contentInSharingWindow.ButtonControl(searchDepth=4, Name="是").Click()

    def share_content_sound_highframerate(self):
        """分享屏幕 不共享声音 1080P"""
        shareContentWindow = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutBackgroundDlg") \
            .WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutCoverDlg") \
            .WindowControl(searchDepth=1, ClassName="ev_app::views::CSelectShareContent")
        contentInSharingWindow = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CbackgroundWidget")

        time.sleep(10)
        self.meetingLabel.Click()
        self.meetingControlToolBar.ButtonControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnShare").Click()
        time.sleep(2)
        shareContentWindow.ButtonControl(searchDepth=2, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CSelectShareContent.toolbar.pBtShare").Click()
        time.sleep(30)
        contentInSharingWindow.TextControl(searchDepth=7, Name="停止分享").Click()
        time.sleep(2)
        contentInSharingWindow.ButtonControl(searchDepth=4, Name="是").Click()

    def share_whiteboard(self):
        """共享白板"""
        shareContentWindow = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutBackgroundDlg") \
            .WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutCoverDlg") \
            .WindowControl(searchDepth=1, ClassName="ev_app::views::CSelectShareContent")
        time.sleep(10)
        self.meetingLabel.Click()
        self.meetingControlToolBar.ButtonControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnShare").Click()
        time.sleep(2)
        shareContentWindow.TextControl(searchDepth=7, Name="白板").Click()
        time.sleep(2)
        shareContentWindow.ButtonControl(searchDepth=2, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CSelectShareContent.toolbar.pBtShare").Click()
        time.sleep(30)
        white_board_window = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::WhiteBoardDlg")
        white_board_window.GroupControl(searchDepth=1, ClassName="ev_app::views::WhiteBoardTopWidget").TextControl(searchDepth=4, Name="停止分享").Click()
        exit_white_board_button = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::WhiteBoardDlg").WindowControl(searchDepth=1, ClassName="ev_app::views::AlertDlg")\
            .ButtonControl(searchDepth=3, Name="是")
        if exit_white_board_button.Exists():
            exit_white_board_button.Click()

    def switch_video_layout(self):
        """分屏切换"""
        time.sleep(10)
        self.meetingLabel.Click()
        self.meetingControlToolBar.CheckBoxControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnSwitchLayout").Click()

    def __change_name_window(self, rename_window):
        """ 调出更名窗口 """
        time.sleep(10)
        self.meetingLabel.Click()
        self.meetingControlToolBar.ButtonControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnMore").Click()
        time.sleep(1)
        self.meetingControlToolBar.ButtonControl(searchDepth=2, Name="改名").Click()
        time.sleep(2)
        rename_window.EditControl(searchDepth=2, AutomationId="CChangeNameWidget.verticalWidget_2.m_pInputNewNameEdit").Click()

    def rename(self, new_name):
        """改名"""
        rename_window = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CChangeNameWidget")
        self.__change_name_window(rename_window)
        time.sleep(1)
        rename_window.EditControl(searchDepth=2, AutomationId="CChangeNameWidget.verticalWidget_2.m_pInputNewNameEdit").SendKeys(new_name)
        rename_window.ButtonControl(searchDepth=2, AutomationId="CChangeNameWidget.m_pBottomView.m_pSureButton").Click()

    def rename_enter_key(self, new_name):
        """改名 === 名字里面包含 {ENTER}"""
        rename_window = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CChangeNameWidget")
        self.__change_name_window(rename_window)
        time.sleep(1)
        rename_window.EditControl(searchDepth=2, AutomationId="CChangeNameWidget.verticalWidget_2.m_pInputNewNameEdit").SendKeys(new_name)

    def audio_only(self):
        """切换到语音模式"""
        time.sleep(10)
        self.meetingLabel.Click()
        self.meetingControlToolBar.ButtonControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnMore").Click()
        time.sleep(1)
        self.meetingControlToolBar.ButtonControl(searchDepth=2, Name="切到语音模式").Click()

    def av_escalation(self):
        """切换到视频模式"""
        avEscalationWindow = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutBackgroundDlg") \
            .WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutCoverDlg")
        avEscalationWindow.ButtonControl(searchDepth=2, Name="退出语音模式").Click()

    def change_volume(self):
        """调节音量"""
        time.sleep(10)
        self.meetingLabel.Click()
        self.meetingControlToolBar.CheckBoxControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnVolume").Click()
        auto.PressKey(auto.Keys.VK_UP)
        auto.PressKey(auto.Keys.VK_DOWN)

    def minimise_local_video(self):
        """本地视频最小化"""
        self.meetingControlToolBar.ButtonControl(searchDepth=3,
                                            AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.CLayoutFloatingCellsDlg.m_pWgtTopTitleBar.pBtMin").Click()

    def maximise_local_video(self):
        """恢复本地视频"""
        time.sleep(10)
        self.meetingLabel.Click()
        self.meetingControlToolBar.ButtonControl(searchDepth=2, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.widget.m_pBtnShowPic").Click()

    def maximise_window(self):
        """最大化窗口"""
        time.sleep(10)
        self.meetingWindowControl.ButtonControl(searchDepth=2, AutomationId="CLayoutBackgroundDlg.m_pWgtTitleBar.m_pRightWidget.m_pBtnMax").Click()

    def restore_window_from_maximise(self):
        """恢复先前视窗"""
        time.sleep(10)
        self.meetingWindowControl.ButtonControl(searchDepth=2, AutomationId="CLayoutBackgroundDlg.m_pWgtTitleBar.m_pRightWidget.m_pBtnRestore").Click()

    def video_fullscreen(self):
        """视频全屏"""
        time.sleep(10)
        self.meetingWindowControl.ButtonControl(searchDepth=2, AutomationId="CLayoutBackgroundDlg.m_pWgtTitleBar.m_pRightWidget.m_pBtnFullScreen").Click()

    def video_restore_from_fullscreen(self):
        """恢复先前视频窗口"""
        time.sleep(10)
        x, y = auto.GetCursorPos()
        auto.Click(x + 800, y - 300)
        self.hjtMeetingWindow.WindowControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg")\
            .ButtonControl(searchDepth=4, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pWgtTitleBar.m_pRightWidget.m_pBtnFullScreen_Exit").Click()

    def hangup_call(self):
        """挂断"""
        time.sleep(10)
        self.meetingLabel.Click()
        self.meetingControlToolBar.ButtonControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnHangup").Click()
        time.sleep(2)
        auto.WindowControl(searchDepth=1, ClassName="ev_app::views::AlertDlg").ButtonControl(searchDepth=2, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.AlertDlg.m_bottomWidget.m_button1").Click()

    def terminate_call(self):
        """结束会议"""
        time.sleep(10)
        self.meetingLabel.Click()
        self.meetingControlToolBar.ButtonControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnHangup").Click()
        time.sleep(2)
        auto.WindowControl(searchDepth=1, ClassName="ev_app::views::AlertDlg").ButtonControl(searchDepth=2, Name="结束会议").Click()

    def terminate_call_in_full_mode(self):
        """结束会议"""
        time.sleep(10)
        # auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutBackgroundDlg").WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutCoverDlg")\
        #     .WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutToolbarDlg").WindowControl(searchDepth=3, ClassName="ev_app::views::CLayoutCellCoverDlg").Click()
        x, y = auto.GetCursorPos()
        # Normal PC auto.Click(x+800, y-300)
        # High DPI
        auto.Click(x + 800, y - 300)
        self.meetingControlToolBar.ButtonControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnHangup").Click()
        time.sleep(2)
        auto.WindowControl(searchDepth=1, ClassName="ev_app::views::AlertDlg").ButtonControl(searchDepth=2, Name="结束会议").Click()
