#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input('Insira seu nome:')
while len(nome) <= 3:
    nome = input('Insira seu nome, maior que três caracteres:')

idade = int(input('Insira sua idade:'))
while idade < 0 or idade > 150:
    idade = int(input('Insira sua idade, Entre 0 e 150:'))

salario = float(input('Insira seu salário:'))
while salario <= 0:
    salario = float(input('Insira seu salário:'))

sexo = input('Insira seu sexo "f ou m":')
while sexo != 'f' and sexo != 'm':
    sexo = input('Digite f ou m:')

estado_civil = input('insira seu estado civil em "s,c,v,d":')
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input('insira seu estado civil "s,c,v,d":')