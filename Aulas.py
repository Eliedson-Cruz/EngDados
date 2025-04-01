"""
Guia básico de Python
Autor: Eliedson (ou seu nome)
Descrição: Este script contém exemplos e explicações sobre conceitos essenciais do Python.
"""

# 1. Variáveis e Tipos de Dados
nome = "Eliedson"  # String
idade = 25  # Inteiro
altura = 1.75  # Float
ativo = True  # Booleano

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Ativo: {ativo}")

# 2. Estruturas Condicionais
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# 3. Estruturas de Repetição
for i in range(5):
    print(f"Número {i}")

contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

# 4. Funções
def saudacao(nome):
    """Função que recebe um nome e exibe uma saudação."""
    return f"Olá, {nome}!"

print(saudacao("Eliedson"))

# 5. Listas e Dicionários
lista = [1, 2, 3, 4, 5]
lista.append(6)
print(f"Lista atualizada: {lista}")

pessoa = {"nome": "Eliedson", "idade": 25, "profissao": "Desenvolvedor"}
print(f"Nome: {pessoa['nome']}, Profissão: {pessoa['profissao']}")

# 6. Programação Orientada a Objetos (POO)
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Meu nome é {self.nome} e tenho {self.idade} anos."

p1 = Pessoa("Eliedson", 25)
print(p1.apresentar())

# 7. Manipulação de Arquivos
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Este é um arquivo de exemplo em Python.\n")

with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(f"Conteúdo do arquivo: {conteudo}")

# 8. Uso de Bibliotecas Externas
import math
print(f"Raiz quadrada de 16: {math.sqrt(16)}")

import random
print(f"Número aleatório entre 1 e 10: {random.randint(1, 10)}")

import datetime
print(f"Data e hora atual: {datetime.datetime.now()}")

# 9. Tratamento de Exceções
try:
    numero = int(input("Digite um número: "))
    print(f"O dobro do número é {numero * 2}")
except ValueError:
    print("Erro: Você deve digitar um número válido.")

# 10. Funções Lambda
soma = lambda x, y: x + y
print(f"Soma de 5 e 3: {soma(5, 3)}")

# 11. List Comprehension
quadrados = [x**2 for x in range(10)]
print(f"Quadrados de 0 a 9: {quadrados}")

# 12. Manipulação de Strings
texto = "   Python é incrível!   "
print(texto.strip().upper().replace("INCRÍVEL", "poderoso"))

# 13. Expressões Regulares
import re
email = "exemplo@email.com"
if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
    print("E-mail válido!")
else:
    print("E-mail inválido!")

# 14. JSON (Leitura e Escrita)
import json
dados = {"nome": "Eliedson", "idade": 25, "cidade": "São Paulo"}
json_string = json.dumps(dados)
print(f"JSON: {json_string}")

decodificado = json.loads(json_string)
print(f"Nome decodificado: {decodificado['nome']}")

# 15. Requests (Requisições HTTP)
# Descomente para testar, se necessário
# import requests
# resposta = requests.get("https://api.github.com")
# print(resposta.json())

print("\nGuia básico de Python concluído!")
