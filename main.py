#importando os modulos necessaros pro game
import tkinter as tk 
from time import sleep
from random import randint

#defnndo a tela
win = tk.Tk()
win.title("Jokenpo - Eusébio Simango")
win.geometry("400x400")
win.resizable(False,False)
win.configure(bg="grey")

#dar vida ocomputador
opcoes     = ("PEDRA", "PAPEL", "TESOURA")
#Funcoes
def pedra():
    computador = randint(0,2)
    if   computador == 0:
        tk.Label(win, text="EMPATE", bg="yellow").place(x=50,y=160,width=300,height=200)
    elif computador == 1:
    	tk.Label(win, text=f"VOCE PERDEU, COMPUTADOR JOGOU {(opcoes[computador])}", bg="red").place(x=50,y=160,width=300,height=200)
    elif computador == 2:
    	status = "YOU WIN"
    	tk.Label(win, text=f"VOCE VENCEU, COMPUTADOR JOGOU {(opcoes[computador])}", bg="green").place(x=50,y=160,width=300,height=200)
    #tk.Label(win, text="JOKENPO").place(x=50,y=160,width=300,height=200)
def papel():
    computador = randint(0,2)
    if   computador == 1:
        tk.Label(win, text="EMPATE", bg="yellow").place(x=50,y=160,width=300,height=200)
    elif computador == 2:
    	tk.Label(win, text=f"VOCE PERDEU, COMPUTADOR JOGOU {(opcoes[computador])}", bg="red").place(x=50,y=160,width=300,height=200)
    elif computador == 0:
    	status = "YOU WIN"
    	tk.Label(win, text=f"VOCE VENCEU, COMPUTADOR JOGOU {(opcoes[computador])}", bg="green").place(x=50,y=160,width=300,height=200)
def tesoura():
    computador = randint(0,2)
    if   computador == 2:
        tk.Label(win, text="EMPATE", bg="yellow").place(x=50,y=160,width=300,height=200)
    elif computador == 0:
    	tk.Label(win, text=f"VOCE PERDEU, COMPUTADOR JOGOU {(opcoes[computador])}", bg="red").place(x=50,y=160,width=300,height=200)
    elif computador == 1:
    	status = "YOU WIN"
    	tk.Label(win, text=f"VOCE VENCEU, COMPUTADOR JOGOU {(opcoes[computador])}", bg="green").place(x=50,y=160,width=300,height=200)
    
#command=lambda:def()
"""Butons"""
tk.Button(win, text="PEDRA",   bg="white", fg="red", command=lambda:pedra()).place(x=50,y=50,width=100,height=100)
tk.Button(win, text="PAPEL",   bg="white", fg="blue", command=lambda:papel()).place(x=150,y=50,width=100,height=100)
tk.Button(win, text="TESOURA", bg="white", fg="green", command=lambda:tesoura()).place(x=250,y=50,width=100,height=100)
"""Tela de retorno"""
tk.Label(win, text="JOKENPO").place(x=50,y=160,width=300,height=200)


win.mainloop()
print("closing",end="")
sleep(0.5)
print(".",end="")
sleep(0.5)
print(".",end="")
sleep(0.5)
print(".",end="")


