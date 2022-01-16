# Faça um programa que peça um valor e mostre na tela so o valor é positivo ou negativo

n1 = int(input("Digite um número negativo ou positivo: "))

if n1 > 0:
    print ("Número Positivo")
elif n1 < 0:
    print ("Número Negativo")
else:
    print("Você digitou 0")