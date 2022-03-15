from PyQt5 import uic, QtWidgets

def dados():
    print(win.lineEdit.text())
    dado = win.lineEdit.text()
    win.listWidget.addItem(dado)
    win.lineEdit.clear()
    
def apagar():
    win.lineEdit.clear()
    win.listWidget.clear()
    
#def vazio():
 #   global teste
  #  win.pushButton.setEnabled(True)
   # print('')
loop = True
while loop:
    app = QtWidgets.QApplication([])
    win = uic.loadUi('win0008.ui')


    win.pushButton.clicked.connect(dados)
    win.pushButton_2.clicked.connect(apagar)
    win.lineEdit.setText('digite algo')
    if len(win.lineEdit.text()) > 0:
        #teste = win.lineEdit
        #teste.stateChanged.connect(vazio)
        win.pushButton.setEnabled(True)
    else:
        win.pushButton.setEnabled(False)

    win.show()
    app.exec_()
