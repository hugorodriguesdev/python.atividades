import os
os.system ("cls")

print("Salário do Professor")

nome_prof = input("Digite o nome do Professor: ")
nivel_prof = int(input("Digite o nível do Professor: "))
qtd_de_aulas = int(input("Digite a quantidade de aulas por semana: "))

if nivel_prof == 1:
    salario = qtd_de_aulas * 12.00
    print("O salário do professor" ,nome_prof, "é:",salario)

elif nivel_prof == 2:
    salario = qtd_de_aulas * 17.00
    print("O salário do professor" ,nome_prof, "é:",salario)

elif nivel_prof == 3:
    salario = qtd_de_aulas * 25.00
    print("O salário do professor" ,nome_prof, "é:",salario)

else:
    print("Algo deu errado! Verifique as informações novamente!")

input("Pressione <ENTER> para continuar...")