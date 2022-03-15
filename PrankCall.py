import random
import PySimpleGUI

class PrankCall:
    def __init__(self):
        PySimpleGUI.theme('Black')
        layout = [
            [PySimpleGUI.Button('                                   UM NÚMERO                                   ')],
            [PySimpleGUI.Output(size=(50,10))],
        ]
        self.win = PySimpleGUI.Window('PrankCall',layout=layout)
    def Loop(self,WINDOW_CLOSED=None):
        while True:
            event, valores = self.win.read()
            if event == WINDOW_CLOSED:
                break
            if event == '                                   UM NÚMERO                                   ':
                n = '1234567890'
                n2 = random.choices(n,k=int(3))
                N2 = ''.join(n2)
                n3 = random.choices(n,k=int(4))
                N3 = ''.join(n3)
                print(f'(+258) 84 {N2} {N3}')
PrankCall().Loop()