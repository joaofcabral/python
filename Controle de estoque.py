#Estoque.py

#criar lista vazia
produtos= []
quantidades=   []

def menu():
    opcao = -1
    while opcao !=1 or opcao !=2 or opcao !=3 or opcao !=0:
        print('####Teste#######')
        print('#Controle de Estoque Versão 1.0#')
        print('#Desenvolvido por João#')
        print('#1=Cadastrar#')
        print('#2=Listar#')
        print('#3=Apagar#')
        print('#0=Sair#')
        opcao = int(input('Digite a opção?: '))
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            apagar()
        elif opcao == 0:
            sair()
            
        else:
            print('Opcao invalida, tente de novo')

def cadastrar():
    resp ='S'
    while resp == 'S':
        nome = input('Digite o nome do produto: ')
        if nome in produtos:
            print('Produto já cadastrado')
            continue
        #pede a quantidade e converte para inteiro

        quant = int(input('Digite a quantidade: '))

        #adiciona o produto na lista

        produtos.append(nome)

        #adiciona a quantidade na lista
        quantidades.append(quant)
        
        resp = input('Deseja continuar cadastrando? (S)im ou (N)ão: ').upper()


def listar():
    print('Lista de produtos:')
    print(produtos)
    print ('Quantidade:')
    print(quantidades)
    resp = input('Voltar ao Menu? (S)im ou (N)ão: ').upper()
    
    if resp == 'S':
        menu()

    if resp == 'N':
        sair ();
def sair():
    print("Fechando...")

def apagar():
    resp ='S'
    while resp == 'S':
          
        nome = input('Nome do produto para apagar do estoque: ')
        produtos.remove(nome)
        resp = input('Deseja continuar apagando? (S)im ou (N)ão: ').upper()

menu()



