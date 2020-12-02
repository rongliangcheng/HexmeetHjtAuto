import uiautomation as auto
from time import sleep
from HJT_pkg.HjtWindowsSingleton import HjtWindowSingleton


class JoinAMeeting:

    def __init__(self):
        # print("__init__")
        self.hexMeetHJTWindow = HjtWindowSingleton().getHJTWindow()

    def __join_from_panel(self, mute="false"):
        # print("_clickJoinAMeetingFromPanel_")
        self.go_to_meeting_page()
        sleep(10)
        self.hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtContext").TextControl(
            searchDepth=9, Name="加入会议").Click()
        sleep(2)
        self.mute_audio(mute)
        self.mute_camera(mute)
        sleep(1)
        self.hexMeetHJTWindow.WindowControl(searchDepth=1, AutomationId="CHomeDlg.CJoinConfDlg").GroupControl(
            searchDepth=1, AutomationId="CHomeDlg.CJoinConfDlg.m_pWgtContent") \
            .ButtonControl(searchDepth=3,
                           AutomationId="CHomeDlg.CJoinConfDlg.m_pWgtContent.CLoginJoinConfForm.verticalWidget.m_pBtnJoinConf").Click()

    def go_to_meeting_page(self):
        self.hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtOperationBar").ListControl(
            searchDepth=2, ClassName="ev_app::custom_controls::CHomeMenuListView").Click()
        x, y = auto.GetCursorPos()
        auto.Click(x, y - 70)

    def mute_audio(self, enable="true"):
        mute_audio_checkbox = self.hexMeetHJTWindow.WindowControl(searchDepth=1, AutomationId="CHomeDlg.CJoinConfDlg").GroupControl(
            searchDepth=1, AutomationId="CHomeDlg.CJoinConfDlg.m_pWgtContent") \
            .CheckBoxControl(searchDepth=3,
                           AutomationId="CHomeDlg.CJoinConfDlg.m_pWgtContent.CLoginJoinConfForm.verticalWidget.m_pChkBoxDisableMic")
        if mute_audio_checkbox.GetTogglePattern().ToggleState == 0 and enable == "true":
            mute_audio_checkbox.Click()
        if mute_audio_checkbox.GetTogglePattern().ToggleState == 1 and enable == "false":
            mute_audio_checkbox.Click()

    def mute_camera(self, enable="true"):
        mute_camera_checkbox = self.hexMeetHJTWindow.WindowControl(searchDepth=1, AutomationId="CHomeDlg.CJoinConfDlg").GroupControl(
            searchDepth=1, AutomationId="CHomeDlg.CJoinConfDlg.m_pWgtContent") \
            .CheckBoxControl(searchDepth=3,
                             AutomationId="CHomeDlg.CJoinConfDlg.m_pWgtContent.CLoginJoinConfForm.verticalWidget.m_pChkBoxDisableCamera")
        if mute_camera_checkbox.GetTogglePattern().ToggleState == 0 and enable == "true":
            mute_camera_checkbox.Click()
        if mute_camera_checkbox.GetTogglePattern().ToggleState == 1 and enable == "false":
            mute_camera_checkbox.Click()

    def join_a_meeting_from_top_menu(self, mute="false"):
        # print("_clickJoinAMeetingFromTopMenu_")
        self.go_to_meeting_page()
        sleep(10)
        self.hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtTitleBar").ButtonControl(
            searchDepth=1,
            AutomationId="CHomeDlg.m_pWgtTitleBar.m_pBtnJoinConf").Click()
        sleep(2)
        self.mute_audio(mute)
        self.mute_camera(mute)
        sleep(1)
        self.hexMeetHJTWindow.WindowControl(searchDepth=1, AutomationId="CHomeDlg.CJoinConfDlg").GroupControl(
            searchDepth=1, AutomationId="CHomeDlg.CJoinConfDlg.m_pWgtContent") \
            .ButtonControl(searchDepth=3,
                           AutomationId="CHomeDlg.CJoinConfDlg.m_pWgtContent.CLoginJoinConfForm.verticalWidget.m_pBtnJoinConf").Click()

    def join_a_meeting_from_panel(self, mute="false"):
        self.__join_from_panel(mute)

    def join_a_meeting_from_panel_with_password(self, password):
        # print("_clickJoinAMeetingFromPanel_")
        self.__join_from_panel()
        sleep(2)
        input_password_form = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CInputPasswordWidget")
        input_password_form.EditControl(searchDepth=2,
                                        AutomationId="CInputPasswordWidget.verticalWidget_2.m_pInputPasswordEdit").Click()
        input_password_form.EditControl(searchDepth=2, AutomationId="CInputPasswordWidget.verticalWidget_2.m_pInputPasswordEdit").SendKeys(password + "{ENTER}")

    def join_a_meeting_from_panel_with_password_one_line(self, password, mute="false"):
        self.go_to_meeting_page()
        sleep(10)
        self.hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtContext").TextControl(
            searchDepth=9, Name="加入会议").Click()
        sleep(1)
        self.hexMeetHJTWindow.WindowControl(searchDepth=1, ClassName="ev_app::views::CJoinConfDlg").TextControl(searchDepth=2, Name="加入会议").Click()
        self.mute_audio(mute)
        self.mute_camera(mute)
        # 通过移动鼠标到会议号码后面并添加密码
        x, y = auto.GetCursorPos()
        # auto.Click(x+50, y+50)
        # hig DPI
        auto.Click(x + 40, y + 40)
        auto.SendKeys("*"+password+"{ENTER}")

    def is_in_meeting(self):
        return auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutBackgroundDlg").WindowControl(
            searchDepth=1, ClassName="ev_app::views::CLayoutCoverDlg") \
            .GroupControl(searchDepth=2,
                          AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutCellCoverDlg.m_pWgtContent").Exists()
