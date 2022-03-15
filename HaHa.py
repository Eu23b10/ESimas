#                                               SIM/NAO
"""from random import choice; n = ('sim', 'nao', 'sim', 'sim', 'nao', 'nao', 'sim'); print('='*15,'Jogo de Perguntas SIM/NAO','='*15)
while True:
    nn = str(input('pergunta: ')); print(f'resposta: {choice(n)}')"""

#                                           Plano de estudo
"""from random import choice; from time import sleep; disciplinas = ('Matematica', 'Fisica', 'Quimica', 'Intoducao a Filosofia', 'Portugues', 'Ingles', 'Desenho')
while True:
    print(f'agora estude {choice(disciplinas)}')
    sleep(2)
    break"""

#
import time, calendar
while True:
    pergunta1 = input('digite um ano: ')
    """if pergunta1.isalpha() is True:
        break
    if pergunta1.isnumeric() is False:
        break
    pergunta = int(pergunta1.split())
    if calendar.isleap(pergunta) is True:
        print('Bissexto!')
    if calendar.isleap(pergunta) is False:
        print('Nao bissxto!')"""
    print(pergunta1)



