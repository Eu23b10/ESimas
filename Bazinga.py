import PySimpleGUI as g


class HaHa:
    def __init__(self):
        g.theme('Black')
        layout = [
            [g.Text('Espaco Inicial'), g.Input(key='si', size=(4, 1)), g.Text('Espaco Final'),
             g.Input(key='sf', size=(4, 1))],
            [g.Text('Tempo  Inicial'), g.Input(key='ti', size=(4, 1)), g.Text('Tempo  Final'), g.Input(key='tf', size=(4, 1))],
            [g.Button('Velocidade')],
            [g.Output(size=(35,3))],
]        
        self.win = g.Window('Fisica', layout=layout)

    def Loop(self, WIN_CLOSED: object = None):
        while True:
            event, valores = self.win.read()
            tf = float(valores['tf'])
            ti = float(valores['ti'])
            sf = float(valores['sf'])
            si = float(valores['si'])
            vs = sf - si
            vt = tf - ti
            v = vs/vt
            if event == WIN_CLOSED:
                break
            if event == 'Velocidade':
                print(f'{v}m/s')


HaHa().Loop()
