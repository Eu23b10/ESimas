import pyautogui as auto
import pymsgbox, datetime, time
from PIL import ImageGrab
from PyQt5 import uic, QtWidgets
from time import sleep

auto._mouseMoveDrag('move',0,0,20,20,1)
auto.rightClick()
sleep(73)
auto.mouseUp()



"""pymsgbox.alert(text='Não click em nenhuma tecla e nem use o mause depois de clicar em "Ok" pra proceder a instalacao ',title='Sério')
pyautogui.press('win')
sleep(2)
pyautogui.write('camera')
sleep(3)
pyautogui.press('Enter')
sleep(10)
pymsgbox.alert('Essas imagens estao sendo transmitidas em tmpo real no computador do ESimas')


auto._mouseMoveDrag(moveOrDrag='move',x=0,y=0,xOffset=0,yOffset=660,duration=2)
auto.mouseInfo.draw
auto.doubleClick()"""


'''def screenshot():
    arquivo = QtWidgets.QFileDialog.getSaveFileName()[0]
    win.statusbar.set('Image Saved:' + arquivo)
    with open (arquivo+'.png') as a:
        a.im
    im.save(filename + '.png', format='png')
    win.statusbar.set('Image Saved:'+arquivo)



data = str(str(datetime.datetime.now())[0:4]+str(datetime.datetime.now())[5:7]+str(datetime.datetime.now())[8:10]+str(datetime.datetime.now())[11:13]+str(datetime.datetime.now())[14:16]+str(datetime.datetime.now())[17:19])
filename = 'screenshot'+data
im = ImageGrab.grab()

app = QtWidgets.QApplication([])
win = uic.loadUi('win0011.ui')
win.setWindowTitle('ScreenShot - ESimas')
win.pushButton.clicked.connect(screenshot)

win.show()
app.exec_()
'''