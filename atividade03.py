import os
os.system ("cls") 

# 1 passo - entrada 
print("Calculadora Simples")

numero01 = int(input("Digite o primeiro número: "))
numero02 = int(input("Digite o segundo número: "))

# 2 passo - processamento (operação)
print("Digite o número da sua operação: ")
operacao = int(input(" se for uma Soma, digite (1), \n se for uma subtração, digite (2), \n se for uma Multiplicação, digite (3), \n se for uma divisão, digite (4) \n"))



if operacao == 1:
    resultado = numero01 + numero02
    print("o resultado da soma é:",resultado) 

elif operacao == 2:
    resultado = numero01 - numero02
    print("o resultado da subtração é:",resultado) 

elif operacao == 3:
    resultado = numero01 * numero02
    print("o resultado da multiplicação é:",resultado)

elif operacao == 4:
    resultado = numero01 / numero02
    print("o resultado da divisão é:",resultado)    

else:
    print("Algo deu errado!...")

input("Pressione <ENTER> para continuar...")  
  