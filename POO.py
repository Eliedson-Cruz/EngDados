"""
📚 PROGRAMAÇÃO ORIENTADA A OBJETOS (POO) EM PYTHON - RESUMO COMPLETO
Conteúdo baseado no curso "Introdução à POO com Python", incluindo:
- 4 Pilares da POO
- Desafios (Sistema Bancário e Processamento de Imagens)
- Técnicas Avançadas
"""

# ====== 1. ABSTRAÇÃO (ABC) ======
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

# ====== 2. ENCAPSULAMENTO ======
class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial  # Atributo privado

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return f"Depósito de R${valor} realizado."
        return "Valor inválido!"

# ====== 3. HERANÇA ======
class Veiculo:
    def __init__(self, marca):
        self.marca = marca

class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

# ====== 4. POLIMORFISMO ======
class Passaro:
    def voar(self):
        print("Voando!")

class Pinguim(Passaro):
    def voar(self):
        print("Pinguins não voam!")

# ====== DESAFIO: SISTEMA BANCÁRIO ======
class Conta:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.__saldo = saldo

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return f"Saque de R${valor} realizado."
        return "Saldo insuficiente!"

class ContaCorrente(Conta):
    def __init__(self, cliente, saldo, limite):
        super().__init__(cliente, saldo)
        self.limite = limite

# ====== DESAFIO: PROCESSAMENTO DE IMAGENS ======
class ProcessadorImagem:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    @staticmethod
    def redimensionar(largura, altura):
        return f"Imagem redimensionada para {largura}x{altura}"

    @classmethod
    def from_url(cls, url):
        # Simulação de download
        nome_arquivo = url.split("/")[-1]
        return cls(nome_arquivo)

# ====== TÉCNICAS AVANÇADAS ======
# Classes Abstratas vs. Interfaces
class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQL(DatabaseInterface):
    def connect(self):
        return "Conexão MySQL estabelecida"

# Métodos Mágicos
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas

    def __str__(self):
        return f"Livro: {self.titulo} ({self.paginas} págs)"

    def __len__(self):
        return self.paginas

# ====== DEMONSTRAÇÃO ======
if __name__ == "__main__":
    print("\n=== DEMONSTRAÇÃO POO ===")
    
    # Abstração
    rex = Cachorro()
    print(f"Cachorro faz: {rex.fazer_som()}")
    
    # Encapsulamento
    conta = ContaBancaria(100)
    print(conta.depositar(50))
    print(f"Saldo atual: R${conta.saldo}")
    
    # Polimorfismo
    passaros = [Passaro(), Pinguim()]
    for p in passaros:
        p.voar()
    
    # Métodos Mágicos
    livro = Livro("Python POO", 200)
    print(livro)  # Chama __str__
    print(f"Páginas: {len(livro)}")  # Chama __len__.