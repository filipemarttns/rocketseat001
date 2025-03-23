contatos = []

def adicionar_contato():
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    email = input('Email: ')
    favorito = int(input('Deseja adicionar como favorio?\n'
                        '[1] Sim\n'
                        '[2] Não\n'
                        'Selecione uma das opções acima: '))
            
    contato = {
        nome: nome,
        telefone: telefone,
        email: email,
        favorito: True if favorito == 1 else False
    }
    contatos.append(contato)
    print(f'{nome} adicionado com sucesso!')

def excluir_contato():
    nome = input('Digite o nome do contato que você deseja excluir: ')
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            contatos.remove(contato)
            print(f'{nome} foi removido com sucesso!')
            return
    imprimir_contatos_funcao = (input('Contato não encontrado, deseja ver a lista de contatos?\n'
    '[1] Sim'
    '[2] Não'))
    if imprimir_contatos_funcao == 1:
        print(contatos)
    else:
        excluir_contato()


while True:
    try:
        var_saida = int(input("Seja muito bem-vindo à nossa agenda, escolha uma das opções abaixo:\n"
                              "[1] Adicionar contato\n"
                              "[2] Remover contato\n"
                              "[3] Lista de contatos\n"
                              "[4] Sair\n"
                              "Selecione uma das opções acima: "))
        
        if var_saida == 4:
            print('Muito obrigado por usar nosso calendário!')
            break
        elif var_saida not in [1, 2, 3, 4]:
            print("Opção inválida, tente novamente.")
        elif var_saida == 1:
            adicionar_contato()
        elif var_saida == 2:
            excluir_contato()


    except ValueError:
        print("Por favor, digite um número válido.")