import tkinter as tk
from PIL import ImageGrab
import tkinter.messagebox, datetime,time

def screenshot():
    data = str(str(datetime.datetime.now())[0:4]
               + str(datetime.datetime.now())[5:7]
               + str(datetime.datetime.now())[8:10]
               + str(datetime.datetime.now())[11:13]
               + str(datetime.datetime.now())[14:16]
               + str(datetime.datetime.now())[17:19])
    filename = 'screenshot' + data
    im = ImageGrab.grab()
    im.save(filename + '.png', format='png')
win = tk.Tk()
win.title('ScreenShot - ESimas')
win.geometry('200x50')
win.resizable(False,False)


butao = tk.Button(text='Capturar Tela',command=lambda:screenshot())
butao.place(x=10,y=15,width=180,height=20)




win.mainloop()