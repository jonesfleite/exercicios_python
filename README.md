# REPOSITÓRIO PYTHON BÁSICO EXERCÍCIOS

## Exercícios de prática de Python do básico ao avançado.

1 - Faça um programa que peça dois números e imprima o maior deles.

~~~python

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print (f'O número maior é {n1}')
else:
    print (f'O número maior é {n2}')
~~~

2 - Faça um programa que peça um valor e mostre na tela so o valor é positivo ou negativo.

~~~python

n1 = int(input("Digite um número negativo ou positivo: "))

if n1 > 0:
    print ("Número Positivo")
elif n1 < 0:
    print ("Número Negativo")
else:
    print("Você digitou 0")
~~~

3 -  Faça um programa que verifica se uma letra digitada é "F" ou "M". Conforme a letra digitada escreve: F - Feminino, M - Masculino, Sexo inválido.

~~~python

import re

sexo = input("Digite o seu sexo (F - Feminino , M - Masculino): ")

if re.search("[(Ff)(.eminino)(.EMININO)]", sexo):
    print('Seu sexo é Feminio')
elif re.search("[(Mm)(.asculino)(.ASCULINO)]", sexo):
    print('Seu sexo é Masculino')

~~~



