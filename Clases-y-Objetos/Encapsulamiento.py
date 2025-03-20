class CuentaBancaria:
    def __init__(self, titular:str, saldo_inicial:float = 0):
        self.titular = titular
        self._saldo = saldo_inicial

    def depositar(self, cantidad:float) -> None:
        pass

    def retirar(self, cantidad: float) -> None:
        pass

    def __str__(self) -> str:
        return  f"CuentaBancaria(titular: {self.titular}, saldo: {self._saldo:,.2f})"

if __name__ == '__main__':
        cuenta_lusi = CuentaBancaria("Lusi")
        print(cuenta_lusi)

        @property
        def saldo(self) -> float:
            return self._saldo

        @ saldo.setter
        def saldo(self, nuevo_saldo:float) -> None:
            self._saldo = nuevo_saldo

