#conta.py
class Conta:
    def __init__(self,numero,titular,saldo,limite):
        print("Construindo o objeto...{}".format(self))
        #atributos privados
        self.__numero=numero
        self.__titular=titular
        self.__saldo=saldo
        self.__limite=limite
        self.__dados=numero,titular,saldo,limite
        
    def depositar(self,valor):
        self.__saldo+=valor
        
    def sacar(self,valor):
        if (self.__saldo + self.__limite>=valor):
            self.__saldo-=valor
            return True

        else:
            print("Não há saldo suficiente para sacar")
            return False
    def transferir (self,valor,destino):
        if self.sacar(valor):
            destino.depositar(valor)
        else:
            print("Não há saldo para transferência")
            
        
    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        if self.__saldo<=0:
            self.__limite+=self.__saldo
        else:
            self.__limite

        return self.__limite
    @limite.setter
    def limite(self,limite):
        self.__limite=limite

    #exemplo de método estático
    @staticmethod
    def codigo_banco():
        return "001"
        
contaJoao = Conta(123,'João da Silva',100,1000)
contaZe = Conta(456,'José da Silva',100,1000)

contaJoao.transferir(800,contaZe)
print (contaZe.saldo)
print (contaJoao.saldo)
print (contaJoao.limite)
print (Conta.codigo_banco())
