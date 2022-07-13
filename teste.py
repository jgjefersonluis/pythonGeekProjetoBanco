from models.cliente import Cliente
from models.conta import Conta

felicity: Cliente = Cliente('Felicity Jone', 'felicity@gmail.com', '123.456.789-01', '02/09/1997')
angelina: Cliente = Cliente('Angelina Jolie', 'angelina@gmail.com', '465.456.789-02', '05/11/1999')
airton: Cliente = Cliente('Airton Senna', 'airton@gmail.com', '123.654.987.-03', '25/07/2000')
raimundo: Cliente = Cliente('Raimundo Nonato', 'raimundo@gmail.com', '987.456.789-01', '14/05/2002')

print(felicity)
print(angelina)

contaf: Conta = Conta(felicity)
contaa: Conta = Conta(angelina)
contad: Conta = Conta(airton)
contas: Conta = Conta(raimundo)
