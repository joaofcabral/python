#parametros_nomeados.py


def mensagem(tipo = 'Mensagem', msg = 'Bom dia'):
    print(f'{tipo}: {msg}')


mensagem()
mensagem(msg='Boa tarde')
mensagem(msg='Boa noite')

#end parâmetro nomeado do print

print(1, end='-0-')
print(2, end='-0-')
print(3, end='-0')
