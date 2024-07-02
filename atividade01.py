import os
os.system ("cls")

print("Qual é maior e qual é o menor?")

# 1 passo entrada
valor01 = int(input("Digite o primeiro valor: "))
valor02 = int(input("Digite o segundo valor: "))

# 2 passo - processamento , saida

if valor01 > valor02:
    print("O maior valor é: ",valor01,"e o menor é: ",valor02)

elif valor02 > valor01:
    print("O maior valor é: ",valor02,"E o menor é: ",valor01)   

else:
    print("Os valores são iguais!")     

input("Pressione <ENTER> para continuar...")  