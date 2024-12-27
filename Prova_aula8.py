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
        self.quartos = []  # Lista de quartos
        self.funcionarios = []  # Lista de funcionários
        self.reservas = []  # Lista de reservas

    def cadastrar_funcionario(self, nome, funcao, salario):
        funcionario = Funcionario(nome, funcao, salario)
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f'{funcionario.nome} - {funcionario.funcao} - R${funcionario.salario}')

    def adicionar_quarto(self, numero, diaria, status):
        quarto = Quarto(numero, diaria, status)
        self.quartos.append(quarto)

    def listar_quartos(self):
        for quarto in self.quartos:
            print(quarto.mostrar_status())
    
    def listar_quartos_disponiveis(self):
        quartos_disponiveis = [quarto for quarto in self.quartos if quarto.status == 'Disponível']
        if not quartos_disponiveis:
            print("Não há quartos disponíveis no momento.")
            return
        for quarto in quartos_disponiveis:
            print(quarto.mostrar_status())


class Funcionario:
    def __init__(self, nome, funcao, salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario


class Quarto:
    def __init__(self, numero, diaria, status):
        self.numero = numero
        self.diaria = diaria
        self.status = status

    def mostrar_status(self):
        return f'Quarto {self.numero} - Status: {self.status} - Diária: R${self.diaria}'

    def reservar(self, hospede, num_diarias):
        if self.status == 'Disponível':
            self.status = 'Ocupado'
            reserva = Reserva(self.numero, self.diaria, hospede, num_diarias)
            return reserva
        else:
            print(f'O quarto {self.numero} não está disponível.')
            return None


class Reserva:
    def __init__(self, numero_quarto, diaria, hospede, num_diarias):
        self.numero_quarto = numero_quarto
        self.diaria = diaria
        self.hospede = hospede
        self.num_diarias = num_diarias

    def calcular_conta(self):
        return self.diaria * self.num_diarias


# Criando o hotel
hotel = Hotel()

# Adicionar quartos
hotel.adicionar_quarto(101, 150, 'Disponível')
hotel.adicionar_quarto(102, 150, 'Disponível')
hotel.adicionar_quarto(103, 150, 'Disponível')
hotel.adicionar_quarto(104, 150, 'Disponível')
hotel.adicionar_quarto(105, 150, 'Disponível')


# Menu
while True:
    print('====='*10)
    print('\n\n')
    print("Menu:\n")
    print("[1] - Cadastrar Funcionário")
    print("[2] - Listar Funcionários")
    print("[3] - Listar Quartos Disponíveis")
    print("[4] - Realizar Reserva")
    print("[5] - Valor do Check-out")
    print("[0] - Sair")
    print('\n\n')
    print('====='*10)
    print('\n\n')
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print('\n\n')
        nome = input('Qual o nome do funcionário: ')
        funcao = input(f'Qual a função do funcionário {nome}: ')
        salario = float(input(f'Qual o salário do funcionário {nome}: '))
        hotel.cadastrar_funcionario(nome, funcao, salario)
        print('\n\n')
        continue

    elif opcao == '2':
        print('\n\n')
        print("\nFuncionários:")
        hotel.listar_funcionarios()
        print('\n\n')
        continue

    elif opcao == '3':
        print('\n\n')
        print("\nQuartos disponíveis:")
        hotel.listar_quartos_disponiveis()
        print('\n\n')
        continue

    elif opcao == '4':
        print('\n\n')
        numero_quarto = int(input("\nDigite o número do quarto que deseja reservar: "))
        hospede = input("Qual o nome do hóspede: ")
        num_diarias = int(input("Quantas diárias? "))
        print('\n\n')
        quarto_reservado = None
        for quarto in hotel.quartos:
            if quarto.numero == numero_quarto:
                quarto_reservado = quarto
                reserva = quarto.reservar(hospede, num_diarias)
                if reserva:
                    hotel.reservas.append(reserva)
                    print(f'Reserva realizada para {hospede} no quarto {quarto.numero}.')
                    print(f'Valor total da reserva: R${reserva.calcular_conta()}')
                break
        
        if not quarto_reservado:
            print("Quarto não encontrado ou não disponível.")
        print('\n\n')
        continue

    elif opcao == '5':
        print('\n\n')
        hospede = input("Digite o nome do hóspede para o check-out: ")
        print('\n\n')
        reserva_encontrada = None
        for reserva in hotel.reservas:
            if reserva.hospede.lower() == hospede.lower():
                reserva_encontrada = reserva
                print(f'Nome do hóspede: {reserva.hospede}')
                print(f'Número do quarto: {reserva.numero_quarto}')
                print(f'Diárias: {reserva.num_diarias}')
                print(f'Valor a ser pago: R${reserva.calcular_conta()}')
                break
        
        if not reserva_encontrada:
            print("Reserva não encontrada para esse hóspede.")
            print('\n\n')
            continue

    elif opcao == '0':
        print('\n\n')
        print("Saindo do sistema...")
        print('\n\n')
        print('====='*10)
        break

    else:
        print('\n\n')
        print("Opção inválida! Tente novamente.")
        print('\n\n')
        continue