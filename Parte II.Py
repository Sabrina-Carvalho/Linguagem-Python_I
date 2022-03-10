# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

dia_Semana = input("Que dia é hoje?")
if(dia_Semana == 'domingo' or dia_Semana == 'sábado'):
    print("Hoje é dia de descanso")
else:
    print("Você precisa trabalhar!")


# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

lst = ['Morango', 'Abacaxi', 'Uva', 'Cereja', 'Tangerina', 'Goiaba']
for fruta in lst:
    if (fruta == 'Morango'):
        print("Morango faz parte da lista de frutas")


# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista

tupla = (5, 8, 15, 16)
lst = []
for i in tupla:
    novo_Valor = i * 2
    lst.append(novo_Valor)
print(lst)


# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
for i in range(100, 151, 2):
    print(i)


# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela

temp = 40
while(temp > 35):
    print(temp)
    temp = temp - 1


# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa
count = 0
while(count < 100):
    if(count == 23):
        break
    print(count)
    count += 1


# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista
par = lst = []
var = 4

while(var <= 20):
    par.append(var)
    var += 2
print(par)


# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = range(5, 45, 2)
print(list(nums))


# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')


# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão
# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a 
# vantagem de existir.” (Machado de Assis)

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
count = 0
for caracter in frase:
    if caracter == 'r':
        count += 1
print("O caracter r aparece %s vezes na frase." %(count))




# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e 
# depois faça uma chamada à função para listar os números   

def seq_Num():
    for i in range(2, 21, 2):
        print(i)

seq_Num()


# Exercício 2 - Crie uma função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string

def let_Maius(texto):
    print(texto.upper())
    return

let_Maius('Hello, World')


# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

lista = [1, 2, 3, 4]
def add_List(lista):
    print(lista.append(5))
    print(lista.append(6))
    
add_List(lista)
print(lista)


# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def printNum( arg1, *lista ):
    print (arg1)
    for i in lista:
        print (i)
    return;

# Chamada à função
printNum( 100 )
printNum( 'A', 'B', 'C' )


# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles

soma = lambda arg1, arg2: arg1 + arg2
print ("A soma é : ", soma( 452, 298 ))


# Exercício 6 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda temp: (float(9)/5)* temp + 32, Celsius)
print (list(Fahrenheit))


# Exercício 7
# Crie um dicionário e liste todos os métodos e atributos do dicionário
dic = {}
dir(dic)


# ************* Desafio ************* (pesquise na documentação Python)

# Exercício 8 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo 
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"
import pandas as pd
file_name = "binary.csv"

def retor_Arq(file_name):
    df = pd.read_csv(file_name)
    return df.describe()

retor_Arq(file_name)
 