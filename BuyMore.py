"""produto = str(input('nome do Producto: '))
price = float(input('quanto custa: '))
quantity = int(input('quantas unidades: '))

total = price*quantity

print(f'''
  SuperMarket Buy More Moz


=============================
{quantity} {produto} {price:.2f}Mzn

total a pagar : {total:.2f}Mzn
=============================
Back More Time BuyMore Will 
Be Waiting For You!!!!!!!!@
============================
''')
"""
import PySimpleGUI as g


class BuyMore:
    def __init__(self):
        g.theme('Black')
        layout = [
            [g.Text('                           '), g.Text('BUY MORE MOZ'),  g.Text('                           '),g.Button('Print')],
            [g.Text(' ')],
            [g.Text('Producto   '),g.Input(key='pro')],
            [g.Text('Preco Uni  '),g.Input(key='price')],
            [g.Text('Quantidade'),g.Input(key='Quantity')],
        ]
        self.win = g.Window('BuyMoreMoz',finalize=True,layout=layout)
    def Loop(self, WIN_CLOSED=None):
        while True:
            evento, valores = self.win.read()
            quantidade = int(valores['Quantity'])
            price: float = float(valores['price'])
            total = quantidade*price
            produto = str(valores['pro'])
            if evento == WIN_CLOSED:
                break
            if evento == 'Print':
                self.win.hide()
                g.theme('Black')
                layout =[
                    [g.Output(size=(70,10))]
                ]
                self.win = g.Window('BuyMoreMoz',finalize=True,layout=layout)
                print(f'''
                ============================================
                {quantidade} {produto} {price:.2f}Mzn

                total a pagar: {total:.2f}Mzn
                =============================================
                ''')


BuyMore().Loop()
