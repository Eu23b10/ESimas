from  PyQt5 import uic, QtWidgets
from PyQt5.QtWebEngineWidgets import  QWebEngineView
from PyQt5.QtCore import QUrl, QSize

def win2():
    nome = win.lineEdit.text()
    win_2.show()
    win_2.label.setText('Ola '+nome)
app = QtWidgets.QApplication([])
win = uic.loadUi('win0006.ui')
win_2 = uic.loadUi('win0010.ui')

win.pushButton.clicked.connect(win2)

win.show()
app.exec_()
