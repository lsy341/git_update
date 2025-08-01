from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import pyperclip
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from datetime import datetime

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager



# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])


service = Service(executable_path=ChromeDriverManager().install())

# pyqt 부분
import os

# 변경사항
# 로그인 접속 아이디 리스트
login_dict = {"lsy341" : "thtk6738"}

# 변경사항
# 유효기간 지정

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_PATH = "design.ui"

# 로그인 클래스 생성
class first(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(os.path.join(BASE_DIR, UI_PATH), self)

        # 1) 버튼 클릭 이벤트
        # self.객체이름.clicked.connect(self.실행함수이름)
        self.close_btn.clicked.connect(self.close)



    def close(self):
        sys.exit()

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = first()
main_dialog.show()

sys.exit(app.exec_())
