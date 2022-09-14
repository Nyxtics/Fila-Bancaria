import os
from queue import Queue
from operator import index
from collections import deque
from tkinter.tix import TList 

def limpaTela():
    os.system('cls')

cont = 0 
reserva = 0 
qntd = list(range(1, cont + 1))
excl = list(range(1, reserva + 1))  
while True: 
    print("\n")
    print(f" Existem {len(qntd)} clientes na fila de espera! ")
    print("\n")
    print(f" Senhas a serem chamadas: {qntd} ")
    print("\n")
    print("Digite '1' para adicionar uma pessoa na fila de espera,")
    print("ou '2' para realizar o atendimento. '3' para mostrar ultimas 5 senhas chamadas!!")
    print("\n")
    operação = input("Escolha uma opção: ")
    if operação == "2":
        if len(qntd) > 0:
            chamado = qntd.pop(0)
##################################################################
            reserva += 1
            excl.append(reserva)
###################################################################
            print("\n")
            print(f" A pessoa da senha: {chamado} foi atendida! ")
        else:
            print("\n")
            print("Fila vazia! Ninguém para atender.")
    elif operação == "1":
        cont += 1 
        qntd.append(cont)
    elif operação == "3":
            print("\n")
            print("Ultimas 5 senhas chamadas foram:")
            print(reserva, reserva -1, reserva -2, reserva -3, reserva -4)
    else:
        print("\n")
        print("Digito invalido, digite apenas 1, 2 ou 3.")


#Feito por Josué Augusto e Victor Leonardo Freitas    RA: 1125083

#OBS: Tive dificuldade de fazer funcionar no metodo "FILA CIRCULAR" a funçao "3" do meu codigo professor! "listagem das ultimas senhas"
#Fiz de um outro metodo um pouco mais complicado e aparentemente funcionou bem!