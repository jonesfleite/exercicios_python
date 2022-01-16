# Faça um programa que verifica se uma letra digitada é "F" ou "M". Conforme a letra digitada escreve: F - Feminino, M - Masculino, Sexo inválido
sexo = input("Digite o seu sexo (F - Feminino , M - Masculino): ")

if sexo == "f" or sexo == "F":
    print('Seu sexo é Feminio')
elif sexo == "m" or sexo == "M":
    print('Seu sexo é Masculino')

num1 = int(input("Digite um número: "))
num2 = int(input("Digite mais um número: "))
print (f"A soma do num1 e num2 é: {num1 + num2}")