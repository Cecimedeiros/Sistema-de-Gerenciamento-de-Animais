"""
from first_crud import main1, carregar_abrigo, atualizar_abrigo, buscar_abrigos, excluir_abrigo, cadastrar_abrigo, listar_abrigo, fim
from sec_crud import carregar_animal, atualizar_animal, buscar_animal, excluir_animal, cadastrar_animal, main_animal, carregar_voluntario, buscar_voluntario, cadastrar_voluntario, excluir_voluntario, listar_animal, listar_voluntario, atualizar_voluntario, main_voluntario
from third_crud import carregar_adotantes, cadastrar_adotante, atualizar_adotante, buscar_adotante, excluir_adotante, listar_adotantes, main3

def processo_abrigos():
    carregar_abrigo ()
    cadastrar_abrigo ('nome', 'endereco', 'porte_animal', 'contato')
    listar_abrigo()
    atualizar_abrigo('nome_antigo', 'novo_nome', 'novo_ende', 'novo_porte_animal','novo_contato')
    excluir_abrigo ('nome')
    buscar_abrigos('nome')
    main1()
    fim ()

def processo_volutarios():
    carregar_voluntario()
    cadastrar_voluntario('nome', 'cpf','endereco','contato','horas')
    listar_voluntario ()
    excluir_voluntario('cpf')
    buscar_voluntario('cpf')
    atualizar_voluntario('cpf','novo_nome', 'novo_ende', 'novo_contato', 'novo_horario' )
    main_voluntario()
    carregar_animal()
    cadastrar_animal('nome', 'especie','idade', 'porte', 'raca', 'historico_medico')
    listar_animal()
    atualizar_animal('nome_antigo', 'novo_nome', 'nova_especie', 'nova_idade', 'novo_dono')
    excluir_animal('nome')
    buscar_animal('nome')
    main_animal()

def processo_adotantes():
    carregar_adotantes ()
    cadastrar_adotante ('nome', 'idade', 'cidade', 'contato', 'preferencia_animal')
    listar_adotantes()
    buscar_adotante('nome')
    atualizar_adotante('nome_velho', 'nome_novo', 'end_novo_adotante', 'porte_novo_escolhido','novo_contato_adotante')
    excluir_adotante('nome')
    main3()

def menu():
    print ("\n  <<-------- PLATAFORMA \"EM BUSCA DE UM LAR\" -------->>")
    print ("\n Olá, somos uma plataforma de gerenciamento de animais para adoção. \n \n Conectamos você com abrigos, animais e também recebemos voluntários para nos ajudar nessa causa especial! \n Vamos explorar a plataforma?! " )
    
    op= int(input ("\n Escolha uma opção abaixo: \n 1 - Quero conectar com um abrigo \n 2 - Quero me tornar voluntário(a)/ Sou voluntário(a) da plataforma \n 3 - Quero adotar um animal  \n 4 - Sair da plataforma \n O que deseja fazer no momento? "))

    if op == "1":
        processo_abrigos()
    elif op == "2":
        processo_volutarios()
    elif op == "3":
        processo_adotantes()
    elif op=="4":
        print("Até logo!")
        fim()
        return      
    else:
        print("Opção inválida, tente novamente! ")
        menu()



main1 ()
"""