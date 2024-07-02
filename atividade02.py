import os
os.system ("cls")

print("Numero positivo e negetivo")

# 1 entrada

numero = int(input("Digite um numero: "))

# 2 processamento e saida

if numero > 0:
    print("O número digitado é POSITIVO!")

elif numero < 0:
    print("O número digitado é NEGATIVO!")

else:
    print("O número é ZERO!")      

input("Pressione <ENTER> para continuar...")      