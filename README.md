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

sexo = input("Digite o seu sexo (F - Feminino , M - Masculino): ")

if sexo == "f" or sexo == "F":
    print('Seu sexo é Feminio')
elif sexo == "m" or sexo == "M":
    print('Seu sexo é Masculino')

~~~

[Link dos Exercícios](https://wiki.python.org.br/EstruturaSequencial)

1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.

~~~python

print ("Olá Mundo")

~~~

2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

~~~python
num = input("Digite um número: ")
print (f"O número digitado foi {num}")

~~~

3 - Faça um Programa que peça dois números e imprima a soma.

~~~python
num1 = int(input("Digite um número: "))
num2 = int(input("Digite mais um número: "))
print (f"A soma do num1 e num2 é: {num1 + num2}")

~~~

4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

~~~python
num1 = int(input("Digite a primeira nota: "))
num2 = int(input("Digite a segunda nota: "))
num3 = int(input("Digite a terceira nota: "))

resultado = (num1 + num2 + num3) / 3

print(f"Resultado da média da nota é {resultado}")

~~~
