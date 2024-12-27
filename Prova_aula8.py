# Desenvolva um sistema em Python para gerenciar as operações de um hotel.
# Para isso, você deve criar uma classe chamada Hotel que será responsável por gerenciar os funcionários, as reservas e os quartos.
# O sistema deve ter as seguintes funcionalidades:

# Funcionalidades:
# Gerenciamento de Funcionários:

# A classe Hoteldeve ser capaz de armazenar informações sobre os funcionários do hotel. Para cada funcionário, o sistema deve registrar:
# Nome
# Função (como gerente, recepcionista, limpeza, etc.)
# Salário
# Gerenciamento de Reservas:

# O hotel deve ser capaz de receber reservas de hóspedes, atribuir quartos a essas reservas e calcular a conta final ao final da estadia.
# Cada reserva deve estar associada a:
# Nome do hóspede
# Número de dias de estadia
# Número do quarto atribuído
# Gerenciamento de Quartos:

# O hotel deve manter uma lista de quartos disponíveis e ocupados. Cada quarto deve ter as seguintes informações:
# Número do quarto
# Preço por diária
# Status (disponível ou ocupado)
# Cálculo da Conta Final:

# Ao final da estadia, o sistema deve calcular o valor total a ser pago,
# baseado no número de dias de estadia e no preço da diária do quarto atribuído ao hóspede.

class Hotel:
    def __init__(self):
        self.hotel = 'TS Hotel'
        

class Funcionario(Hotel):
    def __init__(self, nome, funcao, salario):
        super().__init__()
        self.nome = nome
        self.funcao = funcao
        self.salario = salario
    
    def cadastrar(self):
        nome = input('Qual o nome do funcionário: ')
        funcao = input(f'Qual a função do funcionário {nome}: ')
        salario = input(f'Qual o sálario do funcionário {nome}: ')
        return Funcionario(nome , funcao , salario)
        
    
class Reserva(Hotel):
    def __init__(self, numero, diaria, hospede , num_diarias):
        self.hospede = hospede
        self.num_diarias = num_diarias

class Quarto(Reserva):
    def __init__(self, numero, diaria, status):
        super().__ininit__()
        self.numero = numero
        self.diaria = diaria
        self.status = status
        
    def mostrar_status(self):
        return f'Quarto {self.numero} - Status: {self.status}'
    

    def reservar(self):      
        hospede = input('Qual o nome do Hóspede: ')
        num_diarias = int(input('Quantas diárias serão: '))
        self.status = 'Ocupado'
        return Reserva(self.numero,self.diaria,hospede,num_diarias)
    def lista_quarto_disponível(lista_quarto):
    lista_quarto_disponível = []
    for i in lista_quarto:
        if i.status == 'Disponível':
            lista_quarto_disponível.append[i]
    return lista_quarto_disponível
    
    
        
quarto_101 = Quarto(101 , 150 , 'Disponível')
quarto_102 = Quarto(102 , 150 , 'Disponível')
quarto_103 = Quarto(103 , 150 , 'Disponível')
quarto_104 = Quarto(104 , 150 , 'Disponível')
quarto_105 = Quarto(105 , 150 , 'Disponível')
quarto_201 = Quarto(201 , 250 , 'Disponível')
quarto_202 = Quarto(202 , 250 , 'Disponível')
quarto_203 = Quarto(203 , 250 , 'Disponível')
quarto_204 = Quarto(204 , 250 , 'Disponível')
quarto_205 = Quarto(205 , 250 , 'Disponível')

lista_quarto = [quarto_101 , quarto_102 , quarto_103 , quarto_104 , quarto_105 , quarto_201 , quarto_202 , quarto_203 , quarto_204 , quarto_205]









