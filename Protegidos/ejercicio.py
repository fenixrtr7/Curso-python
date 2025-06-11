# Implementar una clase CuentaBancaria con un metodo protegido para actualizar el saldo y un metodo privado para registrar las transacciones 
# internamente

class BankAcount:
    def __init__(self):
        self._money = 1000
        #self.__private_variable = 'Private'

    def _upadet_money(self, add_money):
        self._money += add_money
        self.__transaction()

    def __transaction(self):
        print(f'Movimiento Saldo actual {self._money}')

    def public_method(self):
        self.__private_method()

account = BankAcount()
#print(base._protected_variable)
account._upadet_money(500)
account._upadet_money(1500)
#base.public_method()