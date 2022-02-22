lista = [] #lista vazia

def cadprod(npcadastrar: dict):
    lista.append(npcadastrar)
    return
 # criei uma função para cadastrar um produto específico na lista
 # essa lista irá receber um produto onde esse produto obrigatoriamente
 # deve ser um dicionário para a lista que no inicio está vazia o metodo
 # append é chamado passando como parâmetro o produto para ser cadastrado
 # onde lista receberá mais um valor que é o dicionário, ela irá manter
 # os outros valores e adicionar os novos e irá retornar.

op = int(input('Cadastrar novo produto? 0-Não    1-Sim ')) # pergunta ao usuário se quer fazer um cadastro.
while op == 1: # caso a opção 1 seja inserida o programa pede para inserir um novo produto dentro do dicionário.
    novoprod = {}
    novoprod['codigo'] = int(input('Digite o código do produto: '))
    if novoprod['codigo'] == 0:
        print('Código 0 selecionado, encerrando cadastro de produtos.')
        break # caso o usuário insira o código como 0 o programa é encerrado.
    novoprod['estoque'] = int(input('Digite a quantidade em estoque: '))
    novoprod['minimo'] = int(input('Digite a quantidade mínima do estoque: '))

    cadprod(novoprod)
    # assim que o usuário insere o novo produto, o produto
    # é enviado para a função cadprod como pararâmetro.
    op = int(input('Cadastrar novo produto? 0-Não    1-Sim '))
    # aqui o programa pergunta novamente se o usuário quer cadastrar um novo produto.
if len(lista) > 0: # se a lista for maior do que zero será mostrado a lista na tela.
    print('Lista de produtos por código em ordem crescente:')
    print('CÓDIGO'.center(10), end='')
    # o center e o quebrade linha end foram utilizados para
    # centralizar a palavra e deixar a lista organizada
    print('ESTOQUE'.center(10), end='')
    print('MÍNIMO'.center(10))

    for prod in sorted(lista, key=lambda item: item['codigo']):
        # para cada produto na lista já ordenada será mostrado
        # o codigo, estoque e quantidade minima no estoque.
        print(str(prod['codigo']).center(10), end='')
        print(str(prod['estoque']).center(10), end='')
        print(str(prod['minimo']).center(10))
else:
    print('Lista vazia.')# caso a lista esteja vazia a essa mensagem aparecerá.