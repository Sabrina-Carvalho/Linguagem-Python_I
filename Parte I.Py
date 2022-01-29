# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista


# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista = ['1', '2', '3', '4', '5']
lista


# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
string1 = 'Olá'
string2 = ', Mundo!'
string3 = string1 + string2
string3


# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tupla = (1, 2, 2, 3, 4, 4, 4, 5)
tupla.count(4)


# Exercício 5 - Crie um dicionário vazio e imprima na tela
dicio = {}
dicio


# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dicio = {'Key1': 1, "Key2": 2, 'Key3': 3}
dicio


# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dicio['Key4'] = 4
dicio


# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
dicio = {'key1': 5, 'Key2': 6, 'Key3': [1, 2]}
dicio


# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
lista = ['String', ('x', 'y'), {'key1': '100', 'key02': '200'}, 4.0]
lista

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
# frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
frase [0:18]
Cientista de Dados

# Exercício 11 - Quanto é 7 elevado na potência 4?
7 ** 4
2401


# Exercício 12 - Quanto é 21424 divido por 89?
21424 / 89
240.7191011235955


# Exercício 13 - Imprima a string 'Hello Python de trás pra frente usando indexação.
string = 'Hello Python'
string
string[::-1]
nohtyP olleH

# Exercício 14 - Usando a string "Hello Python" imprima apenas Python.
string = 'Hello Python'
string
string[6:]
Python

# Exercício 15 - Descubra o comprimento da string "Hello Python". Use a função len().
len('Hello Python')
12

# ou 

string = 'Hello Python'
len(string)
12


# Exercício 16 - Quebre a string "Hello Python" em uma lista.
string = "Hello Python"
string.split()
['Hello', 'Python']


# Exercício 17 - Imprima a string "Hello Python" em caixa alta.
string = "Hello Python"
string.upper()
'HELLO PYTHON'


# Exercício 17 - Data a lista a seguir: lst = [1, 2, [3, 4], [5, [100, 200, ['olá']], 23, 11], 1, 7]. Use indexação para obter apenas a string 'olá'. 
lst = [1, 2, [3, 4], [5, [100, 200, ['olá']], 23, 11], 1, 7]
print(lst[3][1][2][0])
olá


# Exercício 18 - Ordene a lista: l = [5, 3, 4, 6, 1]
l = [5, 3, 4, 6, 1]
l.sort()
l
[1, 3, 4, 5, 6]