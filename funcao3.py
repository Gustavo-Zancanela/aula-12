def nome_completo(nome,sobrenome):
    print("Olá, meu nome é",nome,sobrenome)

nome_completo("Luke","Skywalker")
nome_completo("Skywalker","Luke")

nome_completo(nome="James",sobrenome="Bond")
nome_completo(sobrenome="Bond",nome="James")

def adicao(a,b,c):
    print(a,"+",b,"+",c,"=",a+b+c)

adicao(1,2,3)
adicao(c=1,a=2,b=3)
adicao(3,c=1,b=2)

def nome_completo2(nome, sobrenome="Silva"):
    print('Olá, meu nome é', nome,sobrenome)

nome_completo2("Jair","Souza")
nome_completo2("Sandra")
nome_completo2(nome="Roger")

def nome_completo3(nome="Maria", sobrenome="Silva"):
    print('Olá, meu nome é', nome,sobrenome)

nome_completo3("Jair")
nome_completo3()
nome_completo2(nome="Igor")
nome_completo3(sobrenome="Martins")
nome_completo3('Sandro',"Teodoro")

