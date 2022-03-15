from random import choices
import PySimpleGUI as G
class vodacom:
    def __init__(self):
        G.theme('Black')
        layout = [
            [G.Text('Nome'),G.Input(k='name')],
            [G.Text('B.I  N'),G.Input(k='BI')],
            [G.Button('                                        GERAR                                       ')],
            [G.Output(size=(50,10))]
        ]
        self.win = G.Window('GERADOR DE NUMEROS',layout=layout,finalize=True)
    def Loop(self,WIN_CLOSED=None):
        while True:
            n = '012345789'
            event,valores = self.win.read()
            if event == WIN_CLOSED:
                break
            if event == '                                        GERAR                                       ':
                n2 = choices(n,k=int(3))
                n22 = ''.join(n2)
                n3 = choices(n,k=int(4))
                n33 = ''.join(n3)
                nome = str(valores["name"])
                nome1 = nome.upper().rsplit()
                nome2 =''.join(nome1)
                print(f'{nome2}, o seu numero é ',end="")
                print(f'(+258) 84 {n22} {n33}')


vodacom().Loop()
n = '0123456789'
NN = choices(n,k=int(3))
nn = ''.join(NN)
NNN = choices(n,k=int(4))
nnn = ''.join(NNN)
print(f'(+258) 84 {nn} {nnn}')