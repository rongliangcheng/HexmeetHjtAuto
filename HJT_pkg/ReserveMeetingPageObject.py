from HJT_pkg.HjtWindowsSingleton import HjtWindowSingleton
import uiautomation as auto
from time import sleep


class ReserveMeeting:

    def __init__(self):
        self.hexMeetHJTWindow = HjtWindowSingleton().getHJTWindow()
        self.reserve_meeting_page = self.hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtContext")

    def go_to_meeting_page(self):
        self.hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtOperationBar").ListControl(
            searchDepth=2, ClassName="ev_app::custom_controls::CHomeMenuListView").Click()
        x, y = auto.GetCursorPos()
        # auto.Click(x, y - 70)
        # high DPI
        auto.Click(x, y - 55)

    def reserve_meeting_from_panel(self):
        self.go_to_meeting_page()
        self.hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtContext").TextControl(searchDepth=9, Name="预约会议").Click()


    def choose_date(self):
        self.reserve_meeting_page.EditControl(searchDepth=10, Name="请选择开始日期").Click()

    def choose_time(self):
        self.reserve_meeting_page.EditControl(searchDepth=10, Name="请选择开始时间").Click()

    def choose_now(self):
        self.reserve_meeting_page.CheckBoxControl(searchDepth=11, Name="现在").Click()

    def choose_duration(self):
        self.reserve_meeting_page.EditControl(searchDepth=10, Name="请选择时长").Click()

    def fill_password(self, password):
        self.reserve_meeting_page.SpinnerControl(searchDepth=10, Name="12 位以内数字").SendKeys(password)

    def fill_meeting_notes(self, notes):
        self.reserve_meeting_page.EditControl(searchDepth=10, Name="请输入会议备注").SendKeys(notes)

    def choose_participants(self, name):
        self.reserve_meeting_page.ButtonControl(searchDepth=9, Name="+ 选取与会者").Click()
        participants_page = self.reserve_meeting_page.WindowControl(searchDepth=8, Name="选取与会者")

        participants_page.TabItemControl(searchDepth=5, Name="组织结构").Click()
        participants_page.EditControl(searchDepth=4, Name="请选择").Click()
        sleep(1)
        self.hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtContext").TextControl(searchDepth=10, Name="全部类型").Click()
        sleep(1)
        participants_page.EditControl(searchDepth=3, Name="输入用户/终端名称").SendKeys(name)
        sleep(1)
        participants_page.DataItemControl(searchDepth=7, Name=name).Click()
        participants_page.ButtonControl(searchDepth=2, Name="确定").Click()

    def use_random_number_as_meeting_room(self):
        self.reserve_meeting_page.CheckBoxControl(searchDepth=12, Name="使用随机号码作为会议号码").Click()

    def allow_anonymous_user(self):
        self.reserve_meeting_page.CheckBoxControl(searchDepth=11, Name="允许匿名入会").Click()

    def mute_when_join_meeting(self):
        self.reserve_meeting_page.CheckBoxControl(searchDepth=11, Name="加入会议时静音").Click()

    def reserve_confirm(self):
        self.reserve_meeting_page.ButtonControl(searchDepth=10, Name="预约").Click()

    def delete_reserve_meeting(self):
        self.reserve_meeting_page.HyperlinkControl(searchDepth=10, Name="删除").Click()
        sleep(2)
        self.reserve_meeting_page.ButtonControl(searchDepth=9, Name="确定").Click()

    def edit_reserve_meeting(self):
        self.reserve_meeting_page.HyperlinkControl(searchDepth=10, Name="编辑").Click()

    def return_from_edit_reserve(self):
        self.reserve_meeting_page.ButtonControl(searchDepth=7, Name="< 返回").Click()

    def share_reserve_meeting(self):
        self.reserve_meeting_page.HyperlinkControl(searchDepth=10, Name="分享").Click()

    def return_from_share(self):
        self.reserve_meeting_page.ButtonControl(searchDepth=7, Name="< 返回").Click()

    def now_meeting_confirm(self):
        auto.WheelDown(8)
        self.reserve_meeting_page.ButtonControl(searchDepth=10, Name="立即召开").Click()

    def join_now_meeting(self):
        self.reserve_meeting_page.HyperlinkControl(searchDepth=9, Name="加入会议").Click()
        sleep(1)
        self.hexMeetHJTWindow.WindowControl(searchDepth=1, ClassName="ev_app::views::CJoinConfDlg").ButtonControl(searchInterval=4, Name="加入").Click()

    def control_now_meeting(self):
        self.reserve_meeting_page.HyperlinkControl(searchDepth=9, Name="控制会议").Click()


    def invite_others_control_now_meeting(self, name):
        sleep(1)
        self.reserve_meeting_page.ButtonControl(searchDepth=8, Name="邀请").Click()
        sleep(1)
        self.reserve_meeting_page.EditControl(searchDepth=11, Name="输入用户/终端名称").SendKeys(name)
        sleep(1)
        self.reserve_meeting_page.ButtonControl(searchDepth=7, Name="< 返回").Click()
        sleep(1)
        self.reserve_meeting_page.ButtonControl(searchDepth=7, Name="< 返回").Click()

    def terminate_now_meeting(self):
        self.reserve_meeting_page.HyperlinkControl(searchDepth=9, Name="结束").Click()
        sleep(1)
        self.reserve_meeting_page.ButtonControl(searchDepth=8, Name="确定").Click()
