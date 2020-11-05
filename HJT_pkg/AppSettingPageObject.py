import uiautomation as auto
from time import sleep
from HJT_pkg.HjtWindowsSingleton import HjtWindowSingleton


class AppSetting:
    def __init__(self):
        self.hexMeetHJTWindow = HjtWindowSingleton().getHJTWindow()
        self.setting_page = self.hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtContext").GroupControl(searchDepth=2,
                                                                                                                                  AutomationId="CHomeDlg.m_pWgtContext.m_pStackedWgtContent.CSettingsForm")

    def go_to_setting_page(self):
        self.hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtOperationBar").ListControl(searchDepth=2,
                                                                                                                  ClassName="ev_app::custom_controls::CHomeMenuListView").Click()
        x, y = auto.GetCursorPos()
        auto.Click(x, y + 70)

    def chang_bandwidth(self, value):
        """
        values are
        384K,512K,768K,1M,1.5M,2M,3M,4M
        """
        self.go_to_setting_page()
        sleep(3)
        self.setting_page.TextControl(searchDepth=9, Name="呼叫速率").Click()
        x, y = auto.GetCursorPos()
        auto.Click(x, y + 40)
        self.setting_page.ListItemControl(searchDepth=11, Name=value).Click()

    def chang_language(self, language):
        """
        languages are
        English,简体中文
        """
        self.go_to_setting_page()
        sleep(3)
        if self.setting_page.TextControl(searchDepth=9, Name="语言").Exists():
            self.setting_page.TextControl(searchDepth=9, Name="语言").Click()
        else:
            self.setting_page.TextControl(searchDepth=9, Name="Language").Click()

        x, y = auto.GetCursorPos()
        auto.Click(x, y + 40)
        self.setting_page.ListItemControl(searchDepth=11, Name=language).Click()

    def change_snapshot_path(self):
        sleep(3)
        self.go_to_setting_page()
        self.setting_page.ButtonControl(searchDepth=9, AutomationId="CHomeDlg.m_pWgtContext.m_pStackedWgtContent.CSettingsForm.twgtSettingsPages.qt_tabwidget_stackedwidget"
                                                                    ".tabSettingsGeneral.m_pScrollGeneral.qt_scrollarea_viewport.scaSettingsGeneral.scorllGeneralWidght"
                                                                    ".m_pWgtSnapshotPathPanel.m_pBtnChangeSnapshotPath").Click()
        sleep(1)
        self.hexMeetHJTWindow.WindowControl(searchDepth=1, Name="请选择截图文件存放位置:").ButtonControl(searchDepth=1, Name="选择文件夹").Click()

    def change_auto_login(self):
        self.go_to_setting_page()
        self.setting_page.CheckBoxControl(searchDepth=9, Name="自动登录").Click()

    def change_auto_answer(self):
        self.go_to_setting_page()
        self.setting_page.CheckBoxControl(searchDepth=9, Name="自动应答").Click()

    def change_auto_save_white_board_when_exit(self):
        self.go_to_setting_page()
        self.setting_page.CheckBoxControl(searchDepth=9, Name="关闭白板时，自动保存").Click()

    def change_auto_hide_site_name(self):
        self.go_to_setting_page()
        self.setting_page.CheckBoxControl(searchDepth=11, Name="自动隐藏与会者名称显示").Click()

    def change_disable_prompt(self):
        self.go_to_setting_page()
        self.setting_page.CheckBoxControl(searchDepth=10, Name="关闭提示").Click()

    def change_to_full_mode_meeting(self):
        self.go_to_setting_page()
        self.setting_page.TextControl(searchDepth=9, Name="应用").Click()
        auto.WheelDown(5)
        self.setting_page.CheckBoxControl(searchDepth=9, Name="进入会议时全屏显示").Click()
