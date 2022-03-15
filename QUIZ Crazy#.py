import PySimpleGUI as gui
from time import sleep


class crazygame:
    def __init__(self):
        gui.theme('Black')
        layout = [
            [gui.Text('Bem Vindo ao QUIZ DO GCRAZY#, (click OK pra começar)')],
            [gui.Button('OK')],

        ]
        self.win = gui.Window('QUIZ DO GCRAZY#', layout=layout)
    def Loop(self, WIN_CLOSED=None):
        while True:
            evento, valores = self.win.read()
            if evento == WIN_CLOSED:
                break
            if evento == 'OK':
                self.win.hide()
                gui.theme('Black')
                layout = [
                    [gui.Text('Qual é o verdadeiro Nome do GCRAZY#')],
                    [gui.Button('Gildo'), gui.Button('Gabriel'), gui.Button('Geraldo')],
                    [gui.Output(size=(40, 5))]
                ]
                self.win = gui.Window("QUIZ DO GCRAZY#", layout=layout)
            if evento == 'Gildo':
                print('WRONG!! "TENTE NOVAMETE"')
                print('='*30)
            if evento == 'Geraldo':
                print('WRONG!! "TENTE NOVAMETE"')
                print('=' * 30)
            if evento== 'Gabriel':
                print('BOA')
                sleep(2)
                self.win.hide()
                gui.theme('Black')
                layout = [
                    [gui.Text('Qual é o nome do manager do GCRAZY#')],
                    [gui.Button('Daniel'), gui.Button('Tafula'), gui.Button('Eusébio')],
                    [gui.Output(size=(40, 5))]
                ]
                self.win = gui.Window('QUIZ DO GCRAZY#', layout=layout)
            if evento == 'Daniel':
                print('BOA')
                sleep(2)
                self.win.hide()
                gui.theme('Black')
                layout = [
                    [gui.Text('Qual é o surname do manager do GCRAZY#')],
                    [gui.Button('Eusébio'), gui.Button('Frechaut'), gui.Button('Ribeiro')],
                    [gui.Output(size=(40, 5))]
                ]
                self.win = gui.Window('QUIZ DO GCRAZY#', layout=layout)


crazygame().Loop()