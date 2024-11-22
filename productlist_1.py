import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sqlite3

# DB 연결 및 초기화
con = sqlite3.connect("ProductList.db")
cur = con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);"
)

# UI 로드
form_class = uic.loadUiType("ProductList.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # UI 초기화
        self.initializeTable()

        # 초기값 설정
        self.clearInputFields()

        # 이벤트 연결
        self.addButton.clicked.connect(self.addProduct)
        self.updateButton.clicked.connect(self.updateProduct)
        self.deleteButton.clicked.connect(self.removeProduct)
        self.refreshButton.clicked.connect(self.getProduct)
        self.tableWidget.doubleClicked.connect(self.doubleClick)

    def initializeTable(self):
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)

    def addProduct(self):
        try:
            name = self.prodName.text()
            price = self.prodPrice.text()
            if not name or not price.isdigit():
                QMessageBox.warning(self, "입력 오류", "유효한 제품명과 가격을 입력하세요.")
                return
            cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (name, int(price)))
            con.commit()
            self.getProduct()
        except sqlite3.DatabaseError as e:
            QMessageBox.critical(self, "DB 오류", f"데이터베이스 작업 중 오류가 발생했습니다: {e}")

    def updateProduct(self):
        try:
            id_ = self.prodID.text()
            name = self.prodName.text()
            price = self.prodPrice.text()
            if not id_.isdigit() or not name or not price.isdigit():
                QMessageBox.warning(self, "입력 오류", "유효한 제품 ID, 이름, 가격을 입력하세요.")
                return
            cur.execute("UPDATE Products SET Name = ?, Price = ? WHERE id = ?;", (name, int(price), int(id_)))
            con.commit()
            self.getProduct()
        except sqlite3.DatabaseError as e:
            QMessageBox.critical(self, "DB 오류", f"데이터베이스 작업 중 오류가 발생했습니다: {e}")

    def removeProduct(self):
        try:
            id_ = self.prodID.text()
            if not id_.isdigit():
                QMessageBox.warning(self, "입력 오류", "유효한 제품 ID를 입력하세요.")
                return
            cur.execute("DELETE FROM Products WHERE id = ?;", (int(id_),))
            con.commit()
            self.getProduct()
        except sqlite3.DatabaseError as e:
            QMessageBox.critical(self, "DB 오류", f"데이터베이스 작업 중 오류가 발생했습니다: {e}")

    def getProduct(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        cur.execute("SELECT * FROM Products;")
        for row, item in enumerate(cur.fetchall()):
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(item[0])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(item[2])))
        self.clearInputFields()

    def doubleClick(self):
        try:
            self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
            self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
            self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())
        except Exception:
            self.clearInputFields()

    def clearInputFields(self):
        self.prodID.clear()
        self.prodName.clear()
        self.prodPrice.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
