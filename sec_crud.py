import json
import os
from time import sleep


caminho_arquivocrud2 = os.path.join(os.path.dirname(__file__), 'json2.json')


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
        print(f"Nome: {voluntario.get('nome', 'Não informado')},\n Endereço: {voluntario.get('endereço', 'Não informado')},\n Contato: {voluntario.get('contato', 'Não informado')},\n Horas: {voluntario.get('horas', 'Não informado')}, CPF: {voluntario.get('cpf', 'Não informado')} ")

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
            print(f"Nome: {voluntario['nome']}, \n Endereço: {voluntario.get('endereço', 'Não informado')},\n CPF: {voluntario['cpf']}, \n Contato: {voluntario.get('contato', 'Não informado')} \n Horas: {voluntario.get('horas', 'Não informado')}")
            encontrado = True
            break
    if not encontrado:
        print("Nenhum voluntário encontrado!")

        
def atualizar_voluntario(nome_antigo, novo_nome, novo_ende, novo_contato, novo_horario):
    voluntarios = carregar_voluntario()
    for voluntario in voluntarios:
        if voluntario['nome'] == nome_antigo:
            voluntario['nome'] = novo_nome
            voluntario['endereço'] = novo_ende
            voluntario['contato'] = novo_contato
            voluntario['horas'] = novo_horario
            break
    else:
        print("Voluntário não encontrado!")
        return
    with open(caminho_arquivocrud2, 'w', encoding='utf-8') as arquivojson2_aberto: 
        json.dump(voluntarios, arquivojson2_aberto, indent=3, ensure_ascii=False)
    print("Informações sobre o voluntário atualizadas!")
    
    
caminho_arquivocrud_animais = os.path.join(os.path.dirname(__file__), 'animais.json')

def carregar_animal():
    if not os.path.exists(caminho_arquivocrud_animais):

        with open(caminho_arquivocrud_animais, 'w', encoding='utf-8') as arquivojson_animais:
            json.dump([], arquivojson_animais, indent=3)

    with open(caminho_arquivocrud_animais, 'r', encoding='utf-8') as arquivojson_animais:
        return json.load(arquivojson_animais)

def cadastrar_animal(nome, especie, idade, porte, raca, historico_medico, abrigo, caracteristica_animal):
    animais = carregar_animal()
    animais.append({
        'nome': nome,
        'especie': especie,
        'idade': idade,
        'porte': porte,
        'raca': raca,
        'historico_medico': historico_medico,
        'abrigo': abrigo,
        'caracteristica_animal': caracteristica_animal
        
    })
    with open(caminho_arquivocrud_animais, 'w', encoding='utf-8') as arquivojson_animais:
        json.dump(animais, arquivojson_animais, indent=4, ensure_ascii=False)

    print("O animal foi cadastrado!")
    
def listar_animal():
    animais = carregar_animal()
    if not animais:
        print("Nenhum animal cadastrado!")
        return
    for animal in animais:
        print(f"Nome: {animal['nome']}, \n Espécie: {animal['especie']}, \n Idade: {animal['idade']}, \n Porte: {animal['porte']}, \n Raça: {animal['raca']}, \n Histórico Médico: {animal['historico_medico']} \n Abrigo: {animal['abrigo']} \n Características: {animal['caracteristica_animal']}" )

def atualizar_animal(nome_antigo, novo_nome, nova_especie, nova_idade, novo_dono, historico_medico, novo_abrigo, nova_caracteristica_animal):
    animais = carregar_animal()
    nome_antigo = nome_antigo.strip().lower()
    animal_encontrado= False
    for animal in animais:
        if animal['nome'] == nome_antigo:
            animal['nome'] = novo_nome
            animal['especie'] = nova_especie
            animal['idade'] = nova_idade
            animal['dono'] = novo_dono
            animal['historico_medico'] = historico_medico
            animal['abrigo'] = novo_abrigo
            animal['caracteristica_animal'] = nova_caracteristica_animal
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
            dono = animal.get('dono', 'N/A')  # Se não tiver dono, mostra 'N/A'
            print(f"Nome: {animal['nome']}, \nEspécie: {animal['especie']}, \nIdade: {animal['idade']}, \nPorte: {animal['porte']}, \nRaça: {animal['raca']}, \nHistórico Médico: {animal['historico_medico']}, \nAdotado: {adotado}, \nNome do Dono: {dono}")
            encontrado = True
            break
    if not encontrado:
        print("Nenhum animal encontrado!")


def main2():
    while True:
        op = input("\nEscolha uma opção: \n1 - Quero gerenciar voluntários \n2 - Quero gerenciar animais \n3 - Voltar para o menu inicial \n")
        if op == '3':  
            print("Voltando...")
            sleep (2)
            break
        elif op == '1':  
            while True:
                opcao = input("\nDentre as opções abaixo, o que você deseja fazer? \n1 - Cadastrar um voluntário \n2 - Visualizar informações de um voluntário \n3 - Atualizar informações sobre um voluntário \n4 - Excluir informações sobre um voluntário \n5 - Listar os voluntários existentes \n6 - Voltar ao menu secundário\n")
                match opcao:
                    case "1":
                        while True:
                            print("\n->>> CADASTRAMENTO DE VOLUNTÁRIOS - EM BUSCA DE UM LAR <<<-")
                            nome = input("\n Informe o nome completo do voluntário a ser cadastrado: ")
                            while True:
                                try:
                                    cpf = int(input("\n Informe o CPF do voluntário: "))
                                    break
                                except ValueError:
                                    print("CPF inválido! Digite apenas números.")
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
                            
                            while True:                          
                                try:
                                    maisum = input("Deseja cadastrar mais um voluntário (s/n)? ").strip().lower()
                                    
                                    if maisum == 's':
                                        print(" ")
                                        break  
                                    elif maisum == 'n':
                                        print("Voltando para o menu secundário...")
                                        main2 () 
                                    else:
                                        print("Opção inválida! Por favor, digite 's' para sim ou 'n' para não.")
                                
                                except Exception as e:
                                    print(f"Erro inesperado: {e}. Tente novamente.")
                                
                    case "2":
                        while True:
                            print("\n->>> BUSCA DE VOLUNTÁRIOS - EM BUSCA DE UM LAR <<<-")
                            cpf = input("\nInforme o CPF do voluntário a ser procurado: ")
                            buscar_voluntario(cpf)
                        
                            while True:                          
                                try:
                                    maisum = input("Deseja buscar mais um voluntário (s/n)? ").strip().lower()
                                    
                                    if maisum == 's':
                                        print(" ")
                                        break  
                                    elif maisum == 'n':
                                        print("Voltando para o menu secundário...")
                                        main2 () 
                                    else:
                                        print("Opção inválida! Por favor, digite 's' para sim ou 'n' para não.")
                                
                                except Exception as e:
                                    print(f"Erro inesperado: {e}. Tente novamente.")
                    
                    case "3":
                        while True:
                            print("\n->>> ATUALIZAÇÃO DE DADOS DE VOLUNTÁRIOS - EM BUSCA DE UM LAR <<<-")
                            cpf = input("Informe o CPF do voluntário que a ser atualizado: ")
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
                            
                            while True:                          
                                try:
                                    maisum = input("Deseja atualizar mais um voluntário (s/n)? ").strip().lower()
                                    
                                    if maisum == 's':
                                        print(" ")
                                        break  
                                    elif maisum == 'n':
                                        print("Voltando para o menu secundário...")
                                        main2 () 
                                    else:
                                        print("Opção inválida! Por favor, digite 's' para sim ou 'n' para não.")
                                
                                except Exception as e:
                                    print(f"Erro inesperado: {e}. Tente novamente.")
                    case "4":
                        while True:
                            print("\n->>> EXCLUSÃO DE DADOS DE VOLUNTÁRIOS - EM BUSCA DE UM LAR <<<-")
                            cpf = input("Digite o CPF do voluntário que você deseja excluir: ")
                            excluir_voluntario(cpf)
                            
                            while True:                          
                                try:
                                    maisum = input("Deseja excluir mais um voluntário (s/n)? ").strip().lower()
                                    
                                    if maisum == 's':
                                        print(" ")
                                        break  
                                    elif maisum == 'n':
                                        print("Voltando para o menu secundário...")
                                        main2 () 
                                    else:
                                        print("Opção inválida! Por favor, digite 's' para sim ou 'n' para não.")
                                
                                except Exception as e:
                                    print(f"Erro inesperado: {e}. Tente novamente.")                 
                    case "5":
                        print("\n->>> LISTA DE DADOS DE VOLUNTÁRIOS - EM BUSCA DE UM LAR <<<-")
                        listar_voluntario()
                    case "6":
                        print("Voltando ao menu secundário...")
                        sleep (3)
                        break
                    case _:
                        print("Opção inválida! Tente novamente.")
        
        elif op == '2': 
            while True:
                opcao = input("\nDentre as opções abaixo, o que você deseja fazer? \n1 - Cadastrar um animal \n2 - Visualizar informações de um animal \n3 - Atualizar informações sobre um animal \n4 - Excluir informações sobre um animal \n5 - Listar os animais existentes \n6 - Voltar ao menu secundário \n->>> ATENÇÃO: Antes de cadastrar um animal, verifique nossos abrigos disponíveis em Voltar ao Menu Secundário > Menu Principal > Listar Abrigos. ")
                

                match opcao:
                    case "1":
                        while True:
                            print("\n->>> CADASTRAMENTO DE ANIMAIS - EM BUSCA DE UM LAR <<<-")
                            nome = input("\nInforme o nome do animal a ser cadastrado: ")
                            especie = input("\nInforme a espécie do animal: ")
                            idade = input("\nInforme a idade do animal (em anos): ")
                            porte = input("\nInforme o porte do animal (pequeno, médio e grande): ")
                            raca = input("\nInforme a raça do animal: ")
                            abrigo = input ("\nInforme o nome do abrigo em que o animal está instalado: ")
                            historico_medico = input("\n Insira aqui o histórico médico do animal (Ex: Se foi vacinado, castrado, vermifugado...): ")
                            caracteristica_animal = input ("\nDentre as seguintes características: \n companheiro -- bravo -- protetor -- quieto -- agitado -- preguiçoso -- animal de apoio emocional \nDigite duas opções que mais combinam com o animal: ")
                            cadastrar_animal(nome, especie, idade, porte, raca, historico_medico, abrigo, caracteristica_animal)
                            
                            
                            while True:                          
                                try:
                                    maisum = input("Deseja cadastrar mais um animal (s/n)? ").strip().lower()
                                    
                                    if maisum == 's':
                                        print(" ")
                                        break  
                                    elif maisum == 'n':
                                        print("Voltando para o menu secundário...")
                                        main2 () 
                                    else:
                                        print("Opção inválida! Por favor, digite 's' para sim ou 'n' para não.")
                                
                                except Exception as e:
                                    print(f"Erro inesperado: {e}. Tente novamente.")
                                
                                
                    case "2":
                        while True:
                            print("\n->>> BUSCA DE DADOS DE ANIMAIS - EM BUSCA DE UM LAR <<<-")
                            nome = input("\nInforme o nome do animal a ser procurado: ")
                            buscar_animal(nome)
                            maisum = input("Deseja continuar buscando? (s/n): ")
                            
                            while True:                          
                                try:
                                    maisum = input("Deseja buscar mais um animal (s/n)? ").strip().lower()
                                    
                                    if maisum == 's':
                                        print(" ")
                                        break  
                                    elif maisum == 'n':
                                        print("Voltando para o menu secundário...")
                                        main2 () 
                                    else:
                                        print("Opção inválida! Por favor, digite 's' para sim ou 'n' para não.")
                                
                                except Exception as e:
                                    print(f"Erro inesperado: {e}. Tente novamente.")
                                    
                    case "3":
                        while True:
                            print("\n->>> ATUALIZAÇÃO DE DADOS DE ANIMAIS - EM BUSCA DE UM LAR <<<-")
                            animais= carregar_animal ()
                            nome_antigo = input("Informe o nome do animal a ser atualizado (o nome antigo): ")
                            animal_encontrado = any (animal['nome'].strip().lower()==nome_antigo for animal in animais)
                            if not animal_encontrado:
                                print (" Não há informações desse abrigo no nosso sistema!")
                            else: 
                                novo_nome = input("Informe o novo nome: ")
                                nova_especie = input("Informe a nova espécie do animal: ")
                                nova_idade = input("Informe a nova idade do animal: ")
                                historico_medico = input("Informe o novo histórico médico do animal (Ex: Se foi vacinado, castrado, vermifugado...):: ")
                                novo_abrigo = input ("\nInforme o novo nome do abrigo em que o animal está instalado.")
                                nova_caracteristica_animal = input ("\nDentre as seguintes características: \n companheiro -- bravo -- protetor -- quieto -- agitado -- preguiçoso -- animal de apoio emocional \nDigite duas opções que mais combinam com o animal: ")
                                
                                while True:
                                    adotado = input("O animal já foi adotado? (s/n): ").lower()
                                    if adotado == 's':
                                            novo_dono = input("Informe o nome completo do dono do animal: ")
                                            break
                                    elif adotado == 'n':
                                            novo_dono = None
                                            break
                                    else:
                                            print("Opção inválida! Por favor, digite 's' para sim ou 'n' para não.")
                                            continue   
                                atualizar_animal(nome_antigo, novo_nome, nova_especie, nova_idade, novo_dono, historico_medico, novo_abrigo, nova_caracteristica_animal)
                            
                            while True:                          
                                try:
                                    maisum = input("Deseja atualizar informações de mais um animal (s/n)? ").strip().lower()
                                    
                                    if maisum == 's':
                                        print(" ")
                                        break  
                                    elif maisum == 'n':
                                        print("Voltando para o menu secundário...")
                                        main2 () 
                                    else:
                                        print("Opção inválida! Por favor, digite 's' para sim ou 'n' para não.")
                                
                                except Exception as e:
                                    print(f"Erro inesperado: {e}. Tente novamente.")
                            
                    case "4":
                        while True:
                            print("\n->>> EXCLUSÃO DE DADOS DE ANIMAIS - EM BUSCA DE UM LAR <<<-")
                            nome = input("Qual o nome do animal que você deseja excluir? ")
                            excluir_animal(nome)
                            
                            while True:                          
                                try:
                                    maisum = input("Deseja excluir informações de mais um animal (s/n)? ").strip().lower()
                                    
                                    if maisum == 's':
                                        print(" ")
                                        break  
                                    elif maisum == 'n':
                                        print("Voltando para o menu secundário...")
                                        main2 () 
                                    else:
                                        print("Opção inválida! Por favor, digite 's' para sim ou 'n' para não.")
                                
                                except Exception as e:
                                    print(f"Erro inesperado: {e}. Tente novamente.")
                                    
                    case "5":
                        print("\n->>> LISTA DE DADOS DE ANIMAIS - EM BUSCA DE UM LAR <<<-")
                        listar_animal()
                    case "6":
                        print("Voltando ao menu secundário...")
                        break
                    case _:
                        print("Opção inválida! Tente novamente!")   

if __name__ == "__main__":
    main2()