#importando o modulo
import PySimpleGUI as gui
import pygame as pg
from time import sleep
#criando a class
class pessuale:
    #criando a def onde contaram a tela e layout
    def __init__(self):

        gui.theme('Black')
        layout = [
                [gui.Text('Nome'), gui.Input(size=(30,1), key='Nome'), gui.Button('Start')],
                [gui.Button('INTRO DO GCRAZY#')],
                [gui.Output(size=(41,1))]
            ]
        self.win = gui.Window('KMK', layout=layout,finalize=True)
    def Iniciar(self, WIN_CLOSED=None):
        while True:
            evento, valores = self.win.read()
            if evento == WIN_CLOSED:
                break
            if evento == 'Start':
                #print(f'O {valores["Nome"]} diz Heeloo MADAFAKA!')
                layout =[
                    [gui.Text('Nolll'), gui.Input(size=(30, 1), key='Nome'), gui.Button('Startlll')],
                    [gui.Button('gggg#')],
                    [gui.Output(size=(51, 1))]
                ]
                self.win.hide()
                self.win = gui.Window('KMK', layout=layout,finalize=True)
            if evento == 'INTRO DO GCRAZY#':
                pg.init()
                pg.mixer.music.load('better.mp3')
                pg.mixer.music.play()
                sleep(3)
                print('SUUUU',end='')
                sleep(0.5)
                print('KA')

pessuale().Iniciar()