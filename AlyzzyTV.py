import random
import PySimpleGUI as gui
import pymsgbox, sys,traceback
from time import sleep

class PrankCall:
    def __init__(self):
        gui.theme("DarkRed2")
        layout = [
            [gui.Text("                              PRANK-CALL                              ",text_color='white')],
            [gui.Text('Operadora: '),gui.Combo("Movitel Vodacom Tmcel",'selecionar operadora', size=(32,3),key='operadora')],
            [gui.Button("                               Um Número                               ")],
            [gui.Output(size=(44,10),background_color="black",text_color="red")],
        ]
        self.win = gui.Window("ALYZZY TV - PrankCall",layout=layout)
    def Loop(self, WINDOW_CLOSED=None):
        while True:
            evento, valores = self.win.read()
            if evento == WINDOW_CLOSED:
                break
            if evento == "                               Um Número                               ":
                if valores['operadora'] == 'M':
                    n = '1234567890'
                    n2 = random.choices(n,k=int(3))
                    N2 = ''.join(n2)
                    n3 = random.choices(n,k=int(4))
                    N3 = ''.join(n3)
                    print(f'(+258) 86/87 {N2} {N3}')
                if valores['operadora'] == 'o':
                    n = '1234567890'
                    n2 = random.choices(n,k=int(3))
                    N2 = ''.join(n2)
                    n3 = random.choices(n,k=int(4))
                    N3 = ''.join(n3)
                    print(f'(+258) 84/85 {N2} {N3}')
                if valores['operadora'] == 'v':
                    n = '1234567890'
                    n2 = random.choices(n,k=int(3))
                    N2 = ''.join(n2)
                    n3 = random.choices(n,k=int(4))
                    N3 = ''.join(n3)
                    print(f'(+258) 82/83 {N2} {N3}')
                if valores['operadora'] != 'v' and valores['operadora'] != 'M' and valores['operadora'] !='o':
                    print('Selecione Uma Operadora!')
PrankCall().Loop()
pymsgbox.alert(text='''Obrigado! por usares os meus serviços.
                                         -Eusébio Simango''', title='Bazinga',timeout=3000)
sys.exit()
