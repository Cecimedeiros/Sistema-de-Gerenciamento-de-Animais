import json
import os
from time import sleep

caminho_arquivocrud2 = os.path.join(os.path.dirname(__file__), 'voluntarios.json')

def carregar_voluntario():
    if not os.path.exists(caminho_arquivocrud2):
        with open(caminho_arquivocrud2, 'w', encoding='utf-8') as arquivojson2_aberto:
            json.dump([], arquivojson2_aberto, indent=3)
    with open(caminho_arquivocrud2, 'r', encoding='utf-8') as arquivojson2_aberto:
        return json.load(arquivojson2_aberto)

def cadastrar_voluntario(nome, cpf, endereco, contato, horas):
    voluntarios = carregar_voluntario()
    
    voluntarios.append({'nome': nome, 'cpf': cpf, 'endereço': endereco, 'contato': contato, 'horas': horas})
    with open(caminho_arquivocrud2, 'w', encoding='utf-8') as arquivojson2_aberto:
        json.dump(voluntarios, arquivojson2_aberto, indent=3, ensure_ascii=False)
    print("O voluntário foi cadastrado!")
    
def listar_voluntario():
    voluntarios = carregar_voluntario()
    if not voluntarios:
        print("Nenhum voluntário cadastrado!")
        return
    for voluntario in voluntarios:
        print(f" Nome: {voluntario.get('nome', 'Não informado')},\n Endereço: {voluntario.get('endereço', 'Não informado')},\n Contato: {voluntario.get('contato', 'Não informado')},\n Horas: {voluntario.get('horas', 'Não informado')}, \n CPF: {voluntario.get('cpf', 'Não informado')} ")
        print ()

def excluir_voluntario(cpf):
    voluntarios = carregar_voluntario()
    for voluntario in voluntarios:
        if voluntario['cpf'] == cpf:
            voluntarios.remove(voluntario)
            break
    else:
        print("Voluntário não encontrado!")
        return
    with open(caminho_arquivocrud2, 'w', encoding='utf-8') as arquivojson2_aberto:
        json.dump(voluntarios, arquivojson2_aberto, indent=3, ensure_ascii=False)
    print("Dados do voluntário excluídos!")

def buscar_voluntario(cpf):
    voluntarios = carregar_voluntario()
    encontrado = False
    for voluntario in voluntarios:
        if voluntario['cpf'] == cpf:
            print(f"Nome: {voluntario['nome']}, \nEndereço: {voluntario.get('endereço', 'Não informado')},\nCPF: {voluntario['cpf']}, \nContato: {voluntario.get('contato', 'Não informado')} \nHoras: {voluntario.get('horas', 'Não informado')}")
            encontrado = True
            break
    if not encontrado:
        print("Nenhum voluntário encontrado!")
      
def atualizar_voluntario(cpf, novo_nome, novo_ende, novo_contato, novo_horario):
    voluntarios = carregar_voluntario()
    cpf= cpf
    voluntario_encontrado= False
    for voluntario in voluntarios:
        if voluntario['cpf'] == cpf:
            voluntario['nome'] = novo_nome
            voluntario['endereço'] = novo_ende
            voluntario['contato'] = novo_contato
            voluntario['horas'] = novo_horario
            voluntario_encontrado= True
            break
    with open(caminho_arquivocrud2, 'w', encoding='utf-8') as arquivojson2_aberto: 
        json.dump(voluntarios, arquivojson2_aberto, indent=3, ensure_ascii=False)
    if voluntario_encontrado:
        print("Informações sobre o voluntário atualizadas!")
    else:
        print("Voluntário não encontrado!")
        return
   
    
caminho_arquivocrud_animais = os.path.join(os.path.dirname(__file__), 'animais.json')

def carregar_animal():
    if not os.path.exists(caminho_arquivocrud_animais):

        with open(caminho_arquivocrud_animais, 'w', encoding='utf-8') as arquivojson_animais:
            json.dump([], arquivojson_animais, indent=3)

    with open(caminho_arquivocrud_animais, 'r', encoding='utf-8') as arquivojson_animais:
        return json.load(arquivojson_animais)

def cadastrar_animal(nome, especie, idade, porte, raca, historico_medico, abrigo, caracteristica_animal, sexo):
    animais = carregar_animal()
    animais.append({
        'nome': nome,
        'especie': especie,
        'idade': idade,
        'porte': porte,
        'raca': raca,
        'historico_medico': historico_medico,
        'abrigo': abrigo,
        'caracteristica_animal': caracteristica_animal,
        'sexo': sexo
        
    })
    with open(caminho_arquivocrud_animais, 'w', encoding='utf-8') as arquivojson_animais:
        json.dump(animais, arquivojson_animais, indent=4, ensure_ascii=False)

    print("O animal foi cadastrado!")
    
def listar_animal():
    animais = carregar_animal()  
    if not animais:
        print("Nenhum animal cadastrado.")
        return

    for animal in animais:
        
        nome = animal.get('nome', 'Não especificado')
        especie = animal.get('especie', 'Não especificado')
        idade = animal.get('idade', 'Não especificado')
        porte = animal.get('porte', 'Não especificado')
        raca = animal.get('raca', 'Não especificado')
        historico_medico = animal.get('historico_medico', 'Não especificado')
        abrigo = animal.get('abrigo', 'Não especificado')
        caracteristica_animal = animal.get('caracteristica_animal', 'Não especificado')
        sexo = animal.get('sexo', 'Não especificado')
        
        print(f"Nome: {nome}, \nEspécie (1 - Cachorro 2 - Gato 3 - Outro): {especie}, \nIdade (anos): {idade}, \nPorte (1 - Pequeno porte 2 - Médio porte 3 - Grande porte): {porte}, \nRaça: {raca}, \nHistórico Médico: {historico_medico}, \nAbrigo: {abrigo}, \nCaracterísticas: {caracteristica_animal}, \nSexo: {sexo}")
        print()  


def atualizar_animal(nome_antigo, novo_nome, nova_especie, nova_idade, novo_dono, historico_medico, novo_abrigo, nova_caracteristica_animal, novo_sexo, nova_raca):
    animais = carregar_animal()
    nome_antigo = nome_antigo.strip().lower()
    animal_encontrado= False
    for animal in animais:
        if animal['nome'] == nome_antigo:
            animal['nome'] = novo_nome
            animal['especie'] = nova_especie
            animal['idade'] = nova_idade
            animal['raca'] =  nova_raca
            animal['dono'] = novo_dono
            animal['historico_medico'] = historico_medico
            animal['abrigo'] = novo_abrigo
            animal['caracteristica_animal'] = nova_caracteristica_animal
            animal['sexo'] = novo_sexo
            animal_encontrado= True
            break

    with open(caminho_arquivocrud_animais, 'w', encoding='utf-8') as arquivojson_animais:
        json.dump(animais, arquivojson_animais, indent=3, ensure_ascii=False)
    if animal_encontrado: 
        print("Informações sobre o animal atualizadas!")
    else: 
        print (" Animal não encontrado!")

def excluir_animal(nome):
    animais = carregar_animal()
    nome = nome.strip().lower ()
    for animal in animais:
        if animal['nome'].strip().lower() == nome:
            animais.remove(animal)
            break
    else:
        print("Animal não encontrado!")
        return
    with open(caminho_arquivocrud_animais, 'w', encoding='utf-8') as arquivojson_animais:
        json.dump(animais, arquivojson_animais, indent=3, ensure_ascii=False)
    print("Dados do animal excluídos!")

def buscar_animal(nome):
    animais = carregar_animal()
    nome = nome.strip().lower ()
    encontrado = False
    for animal in animais:
        if animal['nome'].strip().lower() == nome:
            adotado = "Sim" if animal.get('dono') else "Não"
            dono = animal.get('dono', 'N/A')  
            print(f"Nome: {animal['nome']}, \nEspécie (1 - Cachorro 2 - Gato 3 - Outro ): {animal['especie']}, \nIdade (anos): {animal['idade']}, \nPorte (1 - Pequeno porte 2 - Médio porte 3 - Grande porte): {animal['porte']}, \nRaça: {animal['raca']}, \nHistórico Médico: {animal['historico_medico']}, \nAdotado: {adotado}, \nNome do Dono: {dono}")
            encontrado = True
            break
    if not encontrado:
        print("Nenhum animal encontrado!")

def voluntario_cadastrar ():
                        
                            print("\n->>> CADASTRAMENTO DE VOLUNTÁRIOS - EM BUSCA DE UM LAR <<<-")
                            nome = input("\n Informe o nome completo do voluntário a ser cadastrado: ")
                            while True:
                                try:
                                    cpf = input("\n Informe o CPF do voluntário: ")
                                    if cpf.isdigit () and len(cpf)==11:
                                        break 
                                    else:
                                        print("CPF inválido! Digite apenas números e com 11 dígitos.")
                                except Exception as e:
                                    print(f"Erro inesperado: {e}. Tente novamente.")
                            endereco = input("\n Informe seu bairro: ")
                            while True:
                                try:
                                    contato = int(input("\n Informe seu melhor contato (apenas em números): "))
                                    break
                                except ValueError:
                                    print("Por favor, digite apenas números para o contato.")
                                    
                            while True:
                                horas = input("\n Informe quantas horas semanais pode dedicar no voluntariado (digite apenas números): ")
                                try:
                                    int(horas)
                                    break
                                except ValueError:
                                    print("Por favor, digite apenas números para as horas.")
                                
                            cadastrar_voluntario(nome, cpf, endereco, contato, horas)

def main_voluntario():  
                    while True:
                        opcao = input("\nDentre as opções abaixo, o que você deseja fazer? \n1 - Visualizar informações de um voluntário \n2 - Atualizar informações sobre um voluntário \n3 - Excluir informações sobre um voluntário \n4 - Listar os voluntários existentes \n5 - Voltar ao menu Inicial \n6 - Sair da plataforma \n")
                        match (opcao):
                                                        
                            case "1":
                                    print("\n->>> BUSCA DE VOLUNTÁRIOS - EM BUSCA DE UM LAR <<<-")
                                    cpf = input("\nInforme o CPF do voluntário a ser procurado: ")
                                    buscar_voluntario(cpf)                             
                            case "2":
                                    print("\n->>> ATUALIZAÇÃO DE DADOS DE VOLUNTÁRIOS - EM BUSCA DE UM LAR <<<-")
                                    cpf = input("Informe o CPF do voluntário que a ser atualizado: ")
                                    voluntarios=carregar_voluntario ()
                                    cpf_encontrado = any (voluntario['cpf']==cpf for voluntario in voluntarios)
                                    if not cpf_encontrado:
                                            print (" Não há informações desse voluntário no nosso sistema!")
                                    else: 
                                        novo_nome = input("Informe o novo nome completo: ")
                                        novo_ende = input("Informe o novo bairro do voluntário: ")
                                        
                                        while True:
                                            novo_contato = input ("Informe o novo contato do voluntário, apenas em números: ")
                                            try:
                                                int(novo_contato)
                                                break
                                            except ValueError:
                                                print("Por favor, digite apenas números para o novo contato.")
                                                
                                        while True:
                                            novo_horario = input("Informe o novo horário disponível, apenas em números: ")
                                            try:
                                                int(novo_horario)
                                                break
                                            except ValueError:
                                                print("Por favor, digite apenas números para o novo horário.") 
                                                
                                        atualizar_voluntario(cpf, novo_nome, novo_ende, novo_contato, novo_horario)               
                            case "3":
                                
                                    print("\n->>> EXCLUSÃO DE DADOS DE VOLUNTÁRIOS - EM BUSCA DE UM LAR <<<-")
                                    cpf = input("Digite o CPF do voluntário que você deseja excluir: ")
                                    excluir_voluntario(cpf)                      
                            case "4":
                                print("\n->>> LISTA DE DADOS DE VOLUNTÁRIOS - EM BUSCA DE UM LAR <<<-")
                                listar_voluntario()     
                            case "5":
                                print("Voltando ao menu inicial...")
                                sleep (2)
                                break
                            case "6":
                                print ("Saindo da plataforma...Até mais! :)")
                                exit()
                            case _:
                                print("Opção inválida! Tente novamente.")

def main_animal():                 
    while True:
        opcao = input("\nDentre as opções abaixo, o que você deseja fazer? \n \n->>> ATENÇÃO: Antes de cadastrar um animal, verifique nossos abrigos disponíveis em 'Voltar ao Menu Secundário' > 'Voltar ao Menu Inicial' > 'Sou voluntário(a) da plataforma e quero gerenciar informações dos abrigos' > 'Listar Abrigos'<<<- \n \n1 - Cadastrar um animal \n2 - Visualizar informações de um animal \n3 - Atualizar informações sobre um animal \n4 - Excluir informações sobre um animal \n5 - Listar os animais existentes \n6 - Voltar ao menu Inicial \n7 - Sair da plataforma \nOpção: ")
       
        match opcao:
            case "1":
                
                    print ("\n ------> CADASTRO DE DADOS DE ANIMAIS - EM BUSCA DE UM LAR <------")
                    nome = input("\nInforme o nome do animal a ser cadastrado: ")
                    while True:
                        especie = input("\nEscolha o número de acordo com a espécie: \n1 - Cachorro \n2 - Gato \n3 - Outro : ")
                   
                        if especie.isdigit() and int(especie) in [1, 2, 3]:
                            especie = str(especie)  
                            break  
                        else:
                            print("Entrada inválida! Por favor, escolha um número entre 1, 2 ou 3.")                  
                    idade = input("\nInforme a idade do animal (em anos): ")
                    while True:
                        porte = input("\nEscolha o número da preferência desejada \n1 - Pequeno porte \n2 - Médio porte \n3 - Grande porte : ")
                    
                        if porte.isdigit() and int(porte) in [1, 2, 3]:
                            porte = str(porte)  
                            break  
                        else:
                            print("Entrada inválida! Por favor, escolha um número entre 1, 2 ou 3.")                   
                    raca = input("\nInforme a raça do animal: ")
                    abrigo = input("\nInforme o nome do abrigo em que o animal está instalado: ")
                    
                    while True:
                        sexo = input("\nInforme o sexo do animal: \n1 - Macho \n2 - Fêmea : ")
                        if sexo == "1":
                            sexo = "macho"
                            break
                        elif sexo == "2":
                            sexo = "fêmea"
                            break
                        else:
                            print("Opção inválida! Por favor, digite '1' para macho ou '2' para fêmea.")
                    
                    print("\nDentre as características:")
                    print("1 - Companheiro\n2 - Bravo\n3 - Protetor\n4 - Quieto\n5 - Agitado\n6 - Preguiçoso\n7 - Animal de apoio emocional")
                    while True:
                        caracteristica_animal = input("Escolha e digite o número da característica que mais combina com o animal: ")
                        if caracteristica_animal in ['1', '2', '3', '4', '5', '6', '7']:
                            break
                        else:
                            print("\nOpção inválida! Escolha um número de 1 a 7.")
                    
                    historico_medico = input("\nInsira aqui o histórico médico do animal (Ex: Se foi vacinado, castrado, vermifugado...): ")
                    
                    cadastrar_animal(nome, especie, idade, porte, raca, historico_medico, abrigo, caracteristica_animal, sexo)
                    
            case "2":
                
                    print("\n->>> BUSCA DE DADOS DE ANIMAIS - EM BUSCA DE UM LAR <<<-")
                    nome = input("\nInforme o nome do animal a ser procurado: ")
                    buscar_animal(nome)
                
            case "3":
                    animais = carregar_animal()
                    print ("\n ------> ATUALIZAÇÃO DE DADOS DOS ANIMAIS - EM BUSCA DE UM LAR <------")
                    nome_antigo = input("Informe o nome do animal a ser atualizado (o nome antigo): ")
                    animal_encontrado = any(animal['nome'].strip().lower() == nome_antigo for animal in animais)
                    if not animal_encontrado:
                        print("Não há informações desse animal no nosso sistema!")
                    else: 
                        novo_nome = input("Informe o novo nome: ")
                        nova_especie = input("Informe o número correspondente â nova espécie do animal (1 - Cachorro -- 2 - Gato -- 3 Outro): ")
                        nova_idade = input("Informe a nova idade do animal: ")
                        nova_raca = input ("Informe a raça do animal: ")
                        while True:
                            novo_sexo = input("Informe o sexo do animal: \n1 - Macho \n2 - Fêmea : ")
                            if novo_sexo == "1":
                                novo_sexo = "macho"
                                break
                            elif novo_sexo == "2":
                                novo_sexo = "fêmea"
                                break
                            else:
                                print("Opção inválida! Por favor, digite '1' para macho ou '2' para fêmea.")
                        
                        print("\nDentre as características:")
                        print("1 - Companheiro\n2 - Bravo\n3 - Protetor\n4 - Quieto\n5 - Agitado\n6 - Preguiçoso\n7 - Animal de apoio emocional")
                        while True:
                            nova_caracteristica_animal = input("Escolha uma característica que mais combina com o animal: ")
                            if nova_caracteristica_animal in ['1', '2', '3', '4', '5', '6', '7']:
                                break
                            else:
                                print("Opção inválida! Escolha um número de 1 a 7.")
                        
                        historico_medico = input("Informe o novo histórico médico do animal (Ex: Se foi vacinado, castrado, vermifugado...): ")
                        novo_abrigo = input("Informe o novo nome do abrigo em que o animal está instalado: ")
                        while True:
                            adotado = input("O animal já foi adotado? (s/n): ").lower()
                            if adotado == 's' or adotado == 'n':
                                break
                            else:
                                print("Opção inválida. Por favor, responda com 's' para sim ou 'n' para não.")

                        novo_dono = input("Informe o nome completo do dono do animal: ") if adotado == 's' else None
                        
                        atualizar_animal(nome_antigo, novo_nome, nova_especie, nova_idade, novo_dono, historico_medico, novo_abrigo, nova_caracteristica_animal, novo_sexo, nova_raca)
                    
            case "4":           
                    print ("\n ------> EXCLUSÃO DE DADOS DOS ANIMAIS - EM BUSCA DE UM LAR <------")
                    nome = input("Qual o nome do animal que você deseja excluir? ")
                    excluir_animal(nome)
            case "5":
                print("\n->>> LISTA DE DADOS DE ANIMAIS - EM BUSCA DE UM LAR <<<-")
                listar_animal()

            case "6":
                print("\nVoltando ao menu inicial...")
                sleep(2)
                return

            case "7":
                print("Saindo da plataforma... Até mais! :)")
                exit()

            case _:
                print("Opção inválida! Tente novamente!")

if __name__ == "_main_":
    main_animal()
    main_voluntario ()