from random import randint
from time import sleep

computador = randint(0, 5)

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar....")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO.....")
sleep(2)

if jogador == computador:
    print("\nPARABENS VOCÊ ADIVINHOU!!!")
else:
    print("\nEU GANHEI, VOCÊ PERDEU !!!\n"
          "Eu pensei no número {} e não no número {}".format(computador, jogador))