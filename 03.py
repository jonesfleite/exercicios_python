# Faça um programa que verifica se uma letra digitada é "F" ou "M". Conforme a letra digitada escreve: F - Feminino, M - Masculino, Sexo inválido
import re

sexo = input("Digite o seu sexo (F - Feminino , M - Masculino): ")

if re.search("[(Ff)(.eminino)(.EMININO)]", sexo):
    print('Seu sexo é Feminio')
elif re.search("[(Mm)(.asculino)(.ASCULINO)]", sexo):
    print('Seu sexo é Masculino')