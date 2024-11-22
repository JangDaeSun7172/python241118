import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QMessageBox
)
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic
import sqlite3
import os

# Initialize database
DB_FILE = "ProductList.db"
if not os.path.exists(DB_FILE):
    with sqlite3.connect(DB_FILE) as con:
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);"
        )

# Load UI file
form_class = uic.loadUiType("ProductList.ui")[0]


class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Initial values
        self.id = 0
        self.name = ""
        self.price = 0

        # Setup TableWidget
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setSortingEnabled(True)  # Allow column sorting
        self.tableWidget.setTabKeyNavigation(False)

        # Connect signals
        self.prodID.returnPressed.connect(self.focusNextChild)
        self.prodName.returnPressed.connect(self.focusNextChild)
        self.prodPrice.returnPressed.connect(self.focusNextChild)
        self.tableWidget.doubleClicked.connect(self.doubleClick)

    def addProduct(self):
        try:
            self.name = self.prodName.text().strip()
            self.price = self.prodPrice.text().strip()

            if not self.name or not self.price.isdigit():
                self.showErrorMessage("Invalid input", "Please enter a valid name and price.")
                return

            with sqlite3.connect(DB_FILE) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (self.name, int(self.price)))
            self.getProduct()
        except Exception as e:
            self.showErrorMessage("Database Error", str(e))

    def updateProduct(self):
        try:
            self.id = self.prodID.text().strip()
            self.name = self.prodName.text().strip()
            self.price = self.prodPrice.text().strip()

            if not self.id.isdigit() or not self.name or not self.price.isdigit():
                self.showErrorMessage("Invalid input", "Please enter valid ID, name, and price.")
                return

            with sqlite3.connect(DB_FILE) as con:
                cur = con.cursor()
                cur.execute("UPDATE Products SET Name = ?, Price = ? WHERE id = ?;", (self.name, int(self.price), int(self.id)))
            self.getProduct()
        except Exception as e:
            self.showErrorMessage("Database Error", str(e))

    def removeProduct(self):
        try:
            self.id = self.prodID.text().strip()

            if not self.id.isdigit():
                self.showErrorMessage("Invalid input", "Please enter a valid ID.")
                return

            with sqlite3.connect(DB_FILE) as con:
                cur = con.cursor()
                cur.execute("DELETE FROM Products WHERE id = ?;", (int(self.id),))
            self.getProduct()
        except Exception as e:
            self.showErrorMessage("Database Error", str(e))

    def getProduct(self):
        try:
            self.tableWidget.clearContents()
            with sqlite3.connect(DB_FILE) as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Products;")
                rows = cur.fetchall()

            self.tableWidget.setRowCount(len(rows))
            for row, data in enumerate(rows):
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(data[0])))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(data[1]))
                itemPrice = QTableWidgetItem(str(data[2]))
                itemPrice.setTextAlignment(Qt.AlignRight)
                self.tableWidget.setItem(row, 2, itemPrice)
        except Exception as e:
            self.showErrorMessage("Database Error", str(e))

    def doubleClick(self):
        try:
            self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
            self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
            self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())
        except Exception as e:
            self.showErrorMessage("Error", str(e))

    def showErrorMessage(self, title, message):
        QMessageBox.critical(self, title, message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    sys.exit(app.exec_())
