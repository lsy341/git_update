from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

# pyqt 부분
import os

# 유효기간 지정

BASE_DIR = os.path.dirname(__file__)
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
