import math as m
import calendar as date

#print(dir(m)) # comando dir pode ser usado para listar as variaveis, funções e constantes

#help(m.log) # comando help pode ser usado para consultar o que cada função faz

# Atividade 1 - Math - 
primeiraquestao_1 = m.cos(m.pi/2) + m.sin(m.pi/2)
print(primeiraquestao_1)

segundaquestao_1 = m.sqrt(3)
print(segundaquestao_1)

terceiraquestao_1 = m.log2(10)
print(terceiraquestao_1)

#Atividade 2 - Calendar - 

#print(dir(date))

primeiraquestao_2 = date.isleap (2018)
print (primeiraquestao_2)

segundaquestao_2 = date.weekday(1992, 5, 22)
nome_dia = date.day_name[segundaquestao_2]
print(nome_dia)

terceiraquestao_2 = date.monthrange(2000, 7)[0]
nome_primeiro = date.day_name[terceiraquestao_2]
print(nome_primeiro)

#Atividade 3 - Variáveis e tipos - 

x_3 = 1
y_3 = 2.3
z_3 = x_3 + y_3 

print(f' A variável {x_3} é do tipo {type(x_3)}\n A variável {y_3} é do tipo {type(y_3)}\n A variável {z_3} é do tipo {type(z_3)}')

x_2 = 1
y_2 = 4
z_2 = x_2 / y_2

print(f'O valor da variável z_3 é de {z_3}')

x_1 = 1.0
y_1 = 4
z_1 = x_1 / y_1

print(f'O valor da variável z_1 é de {z_1}')

peso = 80
def calculo_altura(altura):
    quadrado = m.pow(altura, 2)
    return quadrado

IMC = peso / calculo_altura(1.86)

print (f'O imc calculado foi {IMC}')

# Atividade 4 - Operadores - 

x_4 = 7
print ('x * 2 é maior que 10?')
resultado = x_4 * 2

if resultado > x_4:
    print ('É maior')
else:
    print ('Não é maior')

print ('x / 3 é menor que 5?')
resultado2 = x_4 / 3

if resultado2 < 5:
    print ('É menor')
else:
    print ('É maior')

print ('x / 3 é menor que 5?')
resultado3 = m.pow(x_4, 2)

if resultado3 == 49:
    print ('É igual')
else:
    print ('Não é igual')

y_4 = 3

print ('y é menor que 10 e x é maior que 10?')

if y_4 < 10 and x_4 > 10:
    print('Sim')
else:
    print ('Não')

print(y_4 >= 3 or x_4 == 8)

print(y_4 != 4)

if IMC < 16:
    print('Magreza leve')
elif IMC > 16 and IMC < 17:
    print('Magreza moderada')
elif IMC > 17 and IMC < 18.5:
    print('Magreza leve')
elif IMC > 18.5 and IMC < 25:
    print('Saudavel')
elif IMC > 25 and IMC < 30:
    print('Sobrepeso')
elif IMC > 30 and IMC < 35:
    print('Obesidade Grau 1')
elif IMC > 35 and IMC < 40:
    print('Obesidade Grau 2 (severa)')
else:
    print('Obesidade Grau 3 (mórbida)')

# Atividade 5 - Tipos complexos - 

s = "Curso de graduação Universidade Univille Campus - Joinville!"
print(s[32:40])
print(s[50:60])

print(s[::-1]) # ele inverte a string

# Atividade 6 - Listas - 

pib = [
    ["china", 23120],
    ["usa", 19360],
    ["india", 9447],
    ["japan", 5405],
    ["germany", 4150],
    ["russia", 4000],
    ["indonesia", 3243],
    ["brazil", 3219]
]

pib.append(["turquia", 2974])
print(pib)

pib2 = {
    "china": 23120,
    "usa": 19360,
    "india": 9447,
    "japan": 5405,
    "germany": 4150,
    "russia": 4000,
    "indonesia": 3243,
    "brazil": 3219
}

print(pib2.keys())

valores = pib2.values()
total = sum(pib2.values())
pib2['total'] = total

print(f'{valores}, {total}, {pib2}')
