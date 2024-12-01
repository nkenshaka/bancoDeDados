class Pessoa:
    def __init__(self, id, nome, email):
        self._id = id
        self._nome = nome
        self._email = email

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email


class Funcionario(Pessoa):
    def __init__(self, id, nome, email):
        super().__init__(id, nome, email)

    def add_quarto(self, hotel, quarto):
        hotel.add_quarto(quarto)

    def remover_quarto(self, hotel, quarto):
        hotel.remover_quarto(quarto)

    def registrar_hospede(self, hotel, hospede):
        hotel.registrar_hospede(hospede)

    def cancelar_reserva(self, hotel, reserva):
        hotel.cancelar_reserva(reserva)


class Hospede(Pessoa):
    def __init__(self, id, nome, email):
        super().__init__(id, nome, email)
        self._reservas = []

    def fazer_reserva(self, reserva):
        self._reservas.append(reserva)

    def cancelar_reserva(self, reserva):
        if reserva in self._reservas:
            self._reservas.remove(reserva)

    def consultar_reservas(self):
        return self._reservas


class Quarto:
    def __init__(self, numero, tipo, disponivel=True):
        self._numero = numero
        self._tipo = tipo
        self._disponivel = disponivel

    def reservar(self):
        if self._disponivel:
            self._disponivel = False
            return True
        return False

    def liberar(self):
        self._disponivel = True

    @property
    def numero(self):
        return self._numero

    @property
    def tipo(self):
        return self._tipo

    def esta_disponivel(self):
        return self._disponivel


class Reserva:
    def __init__(self, hospede, quarto):
        self._hospede = hospede
        self._quarto = quarto

    @property
    def hospede(self):
        return self._hospede

    @property
    def quarto(self):
        return self._quarto


class Hotel:
    def __init__(self):
        self._quartos = []
        self._hospedes = []
        self._reservas = []

    def add_quarto(self, quarto):
        self._quartos.append(quarto)

    def remover_quarto(self, quarto):
        if quarto in self._quartos:
            self._quartos.remove(quarto)

    def registrar_hospede(self, hospede):
        self._hospedes.append(hospede)

    def cancelar_reserva(self, reserva):
        if reserva in self._reservas:
            self._reservas.remove(reserva)
            reserva.quarto.liberar()

    def consultar_quartos_disponiveis(self):
        return [quarto for quarto in self._quartos if quarto.esta_disponivel()]

    def realizar_reserva(self, hospede, quarto):
        if quarto.esta_disponivel():
            reserva = Reserva(hospede, quarto)
            self._reservas.append(reserva)
            hospede.fazer_reserva(reserva)
            quarto.reservar()
            print(f"Reserva realizada para o hóspede {hospede.nome} no quarto {quarto.numero}")
            return reserva
        else:
            print(f"O quarto {quarto.numero} não está disponível.")
            return None

# Criando instâncias do sistema
hotel = Hotel()
quarto1 = Quarto(101, "Luxo", True)
quarto2 = Quarto(102, "Simples", True)

# Adicionando quartos ao hotel
funcionario = Funcionario(1, "Carlos", "carlos@email.com")
funcionario.add_quarto(hotel, quarto1)
funcionario.add_quarto(hotel, quarto2)

# Criando hóspede
hospede = Hospede(1, "João", "joao@email.com")

# Registrando hóspede no hotel
funcionario.registrar_hospede(hotel, hospede)

# Fazendo uma reserva
reserva = hotel.realizar_reserva(hospede, quarto1)

# Consultando reservas
print(hospede.consultar_reservas())

# Cancelando reserva
funcionario.cancelar_reserva(hotel, reserva)
