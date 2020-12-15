from HJT_pkg.HjtWindowsSingleton import HjtWindowSingleton
from HJT_pkg.OperateInMeetingPageObject import OperateInMeeting
from time import sleep
import logging

class Contact:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.info("Contact init --")
        self.hexMeetHJTWindow = HjtWindowSingleton().getHJTWindow()
        self.contact_page = self.hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtContext")

    def call_from_favorite(self, name):
        self.log.info("call_from_favorite")
        self.hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtOperationBar").ListControl(searchDepth=2, AutomationId="CHomeDlg.m_pWgtOperationBar.verticalWidget_4.m_pLvMenus").Click()
        self.contact_page.DataItemControl(searchDepth=15, Name=name).Click()
        sleep(1)
        self.contact_page.ButtonControl(searchDepth=11, Name="视频").Click()
        sleep(20)
        operate_in_meeting = OperateInMeeting()
        operate_in_meeting.hangup_call()

    def call_from_organization(self, name):
        self.log.info("call_from_organization")
        self.hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtOperationBar").ListControl(searchDepth=2, AutomationId="CHomeDlg.m_pWgtOperationBar.verticalWidget_4.m_pLvMenus").Click()
        self.contact_page.TabItemControl(searchDepth=14, Name=" 组织结构").Click()
        sleep(1)
        self.contact_page.EditControl(searchDepth=13, Name="输入用户/终端名称").SendKeys(name)
        self.contact_page.DataItemControl(searchDepth=15, Name=name).Click()
        sleep(1)
        self.contact_page.ButtonControl(searchDepth=11, Name="视频").Click()
        sleep(20)
        operate_in_meeting = OperateInMeeting()
        operate_in_meeting.hangup_call()
