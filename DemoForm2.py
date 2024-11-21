import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
# 크롤링
from bs4 import BeautifulSoup
# 웹서버 요청   
import urllib.request as req
# 정규식
import re

# 디자인 파일 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

# 클래스 정의
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.label.setText("첫번째 윈도우")

    def firstClick(self):
        f = open('clien.txt', 'wt', encoding='utf-8')
        for i in range(0, 10):
            url = 'https://www.clien.net/service/board/sold?&od=T31&category=0&po=' + str(i)
            print(url)
            f.write(url + '\n')

            response = req.urlopen(url)
            # 문자열을 받아서
            page = response.read().decode('utf-8')
            # 검색이 용이한 객체 생성
            soup = BeautifulSoup(page, 'html.parser')
            list = soup.find_all('a', attrs={'class':'list_subject'})

            for item in list:
                try:
                    title = item.find('span', attrs={'class':'subject_fixed'})
                    title = title.text.strip()
                    # print(title)
                    if re.search('아이폰', title):
                        f.write(title + '\n')
                        print(title)
                except:
                    pass
        f.close()        
        self.label.setText("중고장터 크롤링 완료")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭~")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭~~")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()