import os
os.system ("cls")

print("calculando desconto")

# 1 passo - entrada

descricao = (input("Digite a descricao do Produto: "))
qtd = int(input("Digite a quantidade de produtos: "))
preco = float(input("Digite o preço unitario do produto: "))

# 2 passo - processamento

# calculando o total sem desconto

total_sem_desconto = qtd * preco

if qtd <= 5:
    desconto = total_sem_desconto * 0.02
    total_com_desconto = total_sem_desconto - desconto
    print("O total sem desconto do" ,descricao, "foi: ",total_sem_desconto)
    print("O seu desconto do" ,descricao, "foi: ",desconto)
    print("Total com desconto do" ,descricao, "foi: ",total_com_desconto)

elif qtd > 5 and qtd <= 10:   
    desconto = total_sem_desconto * 0.03
    total_com_desconto = total_sem_desconto - desconto
    print("O total sem desconto do" ,descricao, "foi: ",total_sem_desconto)
    print("O seu desconto do" ,descricao, "foi: ",desconto)
    print("Total com desconto do" ,descricao, "foi: ",total_com_desconto) 

elif qtd > 10:
    desconto = total_sem_desconto * 0.05
    total_com_desconto = total_sem_desconto - desconto
    print("O total sem desconto do" ,descricao, "foi: ",total_sem_desconto)
    print("O seu desconto do" ,descricao, "foi: ",desconto)
    print("Total com desconto do" ,descricao, "foi: ",total_com_desconto)

else:
    print("Algo deu errado! Verifique as inforções novamente!")     

input("Pressione <ENTER> para continuar...")