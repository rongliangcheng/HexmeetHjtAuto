import time
import subprocess
import os
import win32gui
import win32con
import uiautomation as auto
from time import sleep


class HjtWindowSingleton:
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            print(auto.GetRootControl())
            subprocess.Popen("C:\\Program Files (x86)\\HexMeetHJT\\HexMeetHJT.exe")

        return cls.__instance

    @staticmethod
    def getHJTWindow() -> auto.WindowControl:
        return auto.WindowControl(searchDepth=1, ClassName='ev_app::views::CHomeDlg')

    @staticmethod
    def close_hjt():
        """关闭程序"""
        try:
            hexMeetHJTWindow = auto.WindowControl(searchDepth=1, ClassName='ev_app::views::CHomeDlg')
            if hexMeetHJTWindow.WindowControl(searchDepth=1, ClassName="ev_app::views::AlertDlg").ButtonControl(
                    searchDepth=3, Name="确定").Exists(1):
                hexMeetHJTWindow.WindowControl(searchDepth=1, ClassName="ev_app::views::AlertDlg").ButtonControl(
                    searchDepth=3, Name="确定").Click()
            sleep(3)
            hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtTitleBar").ButtonControl(
                searchDepth=1, AutomationId="CHomeDlg.m_pWgtTitleBar.m_pBtnClose").Click()
            sleep(3)
            hexMeetHJTWindow.WindowControl(searchDepth=1, AutomationId="CHomeDlg.AlertDlg").ButtonControl(searchDepth=3,
                                                                                                          Name="确定").Click()
            sleep(3)

            cmd = 'taskkill /F /IM HexMeetHJT.exe'
            os.system(cmd)
        # if hexMeetHJTWindow.Exists():
        except:
            cmd = 'taskkill /F /IM HexMeetHJT.exe'
            os.system(cmd)

    @staticmethod
    def start_hjt():
        """重启应用"""
        sleep(5)
        if not auto.WindowControl(searchDepth=1, ClassName='ev_app::views::CHomeDlg').Exists():
            subprocess.Popen("C:\\Program Files (x86)\\HexMeetHJT\\HexMeetHJT.exe")

    @staticmethod
    def minimize_windows():
        """最小化所有应用,"""
        """不好用"""
        foreground_window = win32gui.GetForegroundWindow()
        while foreground_window != None:
            print(win32gui.GetWindowText(foreground_window))
            win32gui.ShowWindow(foreground_window, win32con.SW_MINIMIZE)
            foreground_window = win32gui.GetForegroundWindow()


if __name__ == '__main__':
    HjtWindowSingleton.minimize_windows()
