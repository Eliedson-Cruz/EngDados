"""
==================================================
🌟 APRENDA PYTHON PASSO A PASSO - GUIA COMPLETO 🌟
==================================================
Este arquivo contém exemplos práticos e explicações detalhadas 
para você aprender Python desde o básico até conceitos avançados.
"""

# ===========================================================================
# 1️⃣ VARIÁVEIS E TIPOS DE DADOS (FUNDAMENTOS)
# ===========================================================================
print("\n" + "="*60)
print("1️⃣ VARIÁVEIS E TIPOS DE DADOS (FUNDAMENTOS)")
print("="*60)

# 📌 Variáveis são como "caixas" que armazenam informações
nome = "Maria"       # Texto (string) - Sempre entre aspas
idade = 30           # Número inteiro (int)
altura = 1.75        # Número decimal (float)
tem_carro = True     # Valor lógico (bool: True ou False)

# 🔍 Exemplo Prático:
print(f"\n👉 Meu nome é {nome}, tenho {idade} anos e {altura}m de altura.")
print(f"Tenho carro? {'Sim' if tem_carro else 'Não'}")  # Expressão condicional

# 💡 Dica: Use type() para verificar o tipo de uma variável
print(f"\nTipo da variável 'nome': {type(nome)}")
print(f"Tipo da variável 'idade': {type(idade)}")

# ===========================================================================
# 2️⃣ OPERADORES (MATEMÁTICOS, COMPARAÇÃO E LÓGICOS)
# ===========================================================================
print("\n" + "="*60)
print("2️⃣ OPERADORES (MATEMÁTICOS, COMPARAÇÃO E LÓGICOS)")
print("="*60)

# ➕ Operadores Aritméticos
soma = 5 + 3         # 8
subtracao = 10 - 4   # 6
multiplicacao = 2 * 3.5  # 7.0
divisao = 10 / 3     # 3.333... (sempre retorna float)
divisao_inteira = 10 // 3  # 3 (descarta a parte decimal)
resto = 10 % 3       # 1 (resto da divisão)
potencia = 2 ** 3    # 8 (2 elevado a 3)

print(f"\n🔢 Matemática Básica:")
print(f"5 + 3 = {soma}")
print(f"10 / 3 = {divisao:.2f}")  # :.2f formata para 2 casas decimais

# 🔄 Operadores de Comparação (retornam True/False)
igual = 5 == 5       # True
diferente = 5 != 3   # True
maior = 7 > 5        # True
menor_igual = 5 <= 5.0  # True (5 é igual a 5.0)

print("\n🔍 Comparações:")
print(f"5 é igual a 5? {igual}")
print(f"7 é maior que 5? {maior}")

# 🧠 Operadores Lógicos (and, or, not)
e_logico = True and False  # False (ambos precisam ser True)
ou_logico = True or False  # True (apenas um precisa ser True)
negacao = not True         # False (inverte o valor)

print("\n🤔 Lógica Booleana:")
print(f"True AND False = {e_logico}")
print(f"True OR False = {ou_logico}")

# ===========================================================================
# 3️⃣ ESTRUTURAS DE CONTROLE (DECISÕES E REPETIÇÕES)
# ===========================================================================
print("\n" + "="*60)
print("3️⃣ ESTRUTURAS DE CONTROLE (DECISÕES E REPETIÇÕES)")
print("="*60)

# 🌈 Condicionais (if/elif/else)
nota = 7.5

print("\n🎯 Sistema de Notas:")
if nota >= 9:
    print("A - Excelente!")
elif nota >= 7:
    print("B - Bom!")  # Esta linha será executada
elif nota >= 5:
    print("C - Recuperação")
else:
    print("D - Reprovado")

# 🔁 Loops (for e while)
print("\n🔄 Loops:")

# For: Ideal para iterar sobre sequências
print("\n📌 Loop for (0 a 4):")
for i in range(5):  # range(5) = 0, 1, 2, 3, 4
    print(f"Contagem: {i}")

# While: Executa enquanto uma condição for True
print("\n📌 Loop while:")
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1  # Incrementa para evitar loop infinito

# ⏩ Controle de Fluxo (break, continue)
print("\n⏩ Controle de Fluxo:")
for num in range(10):
    if num == 2:
        continue  # Pula o número 2
    if num == 5:
        break     # Interrompe o loop no 5
    print(num)    # Saída: 0, 1, 3, 4

# ===========================================================================
# 4️⃣ ESTRUTURAS DE DADOS (LISTAS, TUPLAS, DICIONÁRIOS, CONJUNTOS)
# ===========================================================================
print("\n" + "="*60)
print("4️⃣ ESTRUTURAS DE DADOS")
print("="*60)

# 🧾 Listas (mutáveis, ordenadas)
frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")        # Adiciona no final
frutas.insert(1, "abacaxi") # Insere na posição 1
frutas.remove("banana")     # Remove pelo valor
ultimo_item = frutas.pop()  # Remove e retorna o último

print("\n🍎 Lista de Frutas:")
for i, fruta in enumerate(frutas, start=1):
    print(f"{i}. {fruta}")

# 🧊 Tuplas (imutáveis)
coordenadas = (-23.5, -46.6)  # Útil para dados fixos
print(f"\n📍 Coordenadas: {coordenadas}")

# 📚 Dicionários (chave-valor)
aluno = {
    "nome": "Carlos",
    "idade": 22,
    "cursos": ["Python", "SQL"],
    "ativo": True
}

print("\n📚 Dicionário de Aluno:")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno.get('idade', 'Não informado')}")

# 🎯 Conjuntos (valores únicos, não ordenados)
numeros = {1, 2, 3, 3, 4}  # Resultado: {1, 2, 3, 4}
print(f"\n🔢 Conjunto: {numeros}")

# ===========================================================================
# 5️⃣ FUNÇÕES (ORGANIZAÇÃO E REUTILIZAÇÃO DE CÓDIGO)
# ===========================================================================
print("\n" + "="*60)
print("5️⃣ FUNÇÕES (ORGANIZAÇÃO E REUTILIZAÇÃO DE CÓDIGO)")
print("="*60)

# 📌 Função Básica
def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal (IMC)"""
    return peso / (altura ** 2)

imc = calcular_imc(70, 1.75)
print(f"\n🔄 IMC calculado: {imc:.2f}")

# 🎭 Função com Parâmetros Opcionais
def saudacao(nome="Visitante"):
    print(f"\n👋 Olá, {nome}!")

saudacao("Ana")  # Saída: "Olá, Ana!"
saudacao()       # Saída: "Olá, Visitante!"

# ===========================================================================
# 6️⃣ TRATAMENTO DE ERROS (EVITANDO FALHAS)
# ===========================================================================
print("\n" + "="*60)
print("6️⃣ TRATAMENTO DE ERROS (EVITANDO FALHAS)")
print("="*60)

try:
    resultado = 10 / 0  # Divisão por zero!
except ZeroDivisionError:
    print("\n❌ Erro: Divisão por zero não permitida!")
else:
    print(f"Resultado: {resultado}")
finally:
    print("✅ Bloco finally sempre executa!")

# ===========================================================================
# 🎉 PARABÉNS! PRÓXIMOS PASSOS:
# ===========================================================================
print("\n" + "="*60)
print("🎉 PARABÉNS! PRÓXIMOS PASSOS:")
print("="*60)

print("""
🚀 O que aprender agora?
1. Módulos e Bibliotecas (requests, pandas, tkinter)
2. Programação Orientada a Objetos (Classes)
3. Projetos Práticos:
   - Jogo da Forca
   - Calculadora
   - Web Scraper
4. Participe de comunidades como Python Brasil!

📚 Recursos Úteis:
- Documentação Oficial: https://docs.python.org/3/
- Exercícios: https://www.w3schools.com/python/python_exercises.asp
""")

print("\n🌟 Fim do tutorial! Agora é sua vez de praticar! 🌟")