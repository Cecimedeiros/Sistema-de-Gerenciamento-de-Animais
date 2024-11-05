import json
import os
from time import sleep

caminho_arquivocrud2 = os.path.join(os.path.dirname(__file__), 'json2.json')


def carregar_voluntario():
    if not os.path.exists(caminho_arquivocrud2):
        with open(caminho_arquivocrud2, 'w') as arquivojson2_aberto:
            json.dump([], arquivojson2_aberto, indent=3)
    with open(caminho_arquivocrud2, 'r') as arquivojson2_aberto:
        return json.load(arquivojson2_aberto)

def cadastrar_voluntario(nome, cpf, endereco, contato, horas):
    voluntarios = carregar_voluntario()
    
    voluntarios.append({'nome': nome, 'cpf': cpf, 'endereço': endereco, 'contato': contato, 'horas': horas})
    with open(caminho_arquivocrud2, 'w') as arquivojson2_aberto:
        json.dump(voluntarios, arquivojson2_aberto, indent=3, ensure_ascii=False)
    print("O voluntário foi cadastrado!")

def listar_voluntario():
    voluntarios = carregar_voluntario()
    if not voluntarios:
        print("Nenhum voluntário cadastrado!")
        return
    for voluntario in voluntarios:
        print(f"Nome: {voluntario['nome']}, \n Endereço: {voluntario['endereço']},\n Contato: {voluntario.get('contato')},\n Horas: {voluntario['horas']}, CPF: {voluntario['cpf']} ")

def excluir_voluntario(nome):
    voluntarios = carregar_voluntario()
    for voluntario in voluntarios:
        if voluntario['nome'] == nome:
            voluntarios.remove(voluntario)
            break
    else:
        print("Voluntário não encontrado!")
        return
    with open(caminho_arquivocrud2, 'w') as arquivojson2_aberto:
        json.dump(voluntarios, arquivojson2_aberto, indent=3, ensure_ascii=False)
    print("Dados do voluntário excluídos!")

def buscar_voluntario(nome):
    voluntarios = carregar_voluntario()
    encontrado = False
    for voluntario in voluntarios:
        if voluntario['nome'] == nome:
            print(f"Nome: {voluntario['nome']}, \n Endereço: {voluntario['endereço']},\n CPF: {voluntario['cpf']}, \n Contato: {voluntario.get('contato')} \n Horas: {voluntario['horas']}")
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
    with open(caminho_arquivocrud2, 'w') as arquivojson2_aberto: 
        json.dump(voluntarios, arquivojson2_aberto, indent=3, ensure_ascii=False)
    print("Informações sobre o voluntário atualizadas!")
    
    
caminho_arquivocrud_animais = os.path.join(os.path.dirname(__file__), 'animais.json')

def carregar_animais():
    if not os.path.exists(caminho_arquivocrud_animais):

        with open(caminho_arquivocrud_animais, 'w') as arquivojson_animais:
            json.dump([], arquivojson_animais, indent=3)

    with open(caminho_arquivocrud_animais, 'r') as arquivojson_animais:
        return json.load(arquivojson_animais)

def cadastrar_animal(nome, especie, idade, porte, raca, historico_medico):
    adotado = ''
    while adotado not in ['s', 'n']:
        adotado = input("O animal é adotado? (s/n): ").lower()
        if adotado == 's':
            nome_dono = input("Informe o nome completo do dono: ")
        elif adotado == 'n':
            nome_dono = None
        else:
            print("Opção inválida! Digite 's' ou 'n'.")

    animais = carregar_animais()
    animais.append({
        'nome': nome,
        'especie': especie,
        'idade': idade,
        'porte': porte,
        'raca': raca,
        'historico_medico': historico_medico,
        'dono': nome_dono
    })
    with open(caminho_arquivocrud_animais, 'w') as arquivojson_animais:
        json.dump(animais, arquivojson_animais, indent=4, ensure_ascii=False)

    print("O animal foi cadastrado!")
    
def listar_animais():
    animais = carregar_animais()
    if not animais:
        print("Nenhum animal cadastrado!")
        return
    for animal in animais:
        print(f"Nome: {animal['nome']}, \n Espécie: {animal['especie']}, \n Idade: {animal['idade']}, \n Porte: {animal['porte']}, \n Raça: {animal['raca']}, \n Histórico Médico: {animal['historico_medico']}")

def atualizar_animal(nome_antigo, novo_nome, nova_especie, nova_idade, novo_dono, historico_medico):
    animais = carregar_animais()
    for animal in animais:
        if animal['nome'] == nome_antigo:
            animal['nome'] = novo_nome
            animal['especie'] = nova_especie
            animal['idade'] = nova_idade
            animal['dono'] = novo_dono
            animal['historico_medico'] = historico_medico  
            break

    with open(caminho_arquivocrud_animais, 'w') as arquivojson_animais:
        json.dump(animais, arquivojson_animais, indent=3, ensure_ascii=False)
    print("Informações sobre o animal atualizadas!")



def excluir_animal(nome):
    animais = carregar_animais()
    for animal in animais:
        if animal['nome'] == nome:
            animais.remove(animal)
            break
    else:
        print("Animal não encontrado!")
        return
    with open(caminho_arquivocrud_animais, 'w') as arquivojson_animais:
        json.dump(animais, arquivojson_animais, indent=3, ensure_ascii=False)
    print("Dados do animal excluídos!")

def buscar_animal(nome):
    animais = carregar_animais()
    encontrado = False
    for animal in animais:
        if animal['nome'] == nome:
            adotado = "Sim" if animal.get('dono') else "Não"
            dono = animal.get('dono', 'N/A')  # Se não tiver dono, mostra 'N/A'
            print(f"Nome: {animal['nome']}, \nEspécie: {animal['especie']}, \nIdade: {animal['idade']}, \nPorte: {animal['porte']}, \nRaça: {animal['raca']}, \nHistórico Médico: {animal['historico_medico']}, \nAdotado: {adotado}, \nNome do Dono: {dono}")
            encontrado = True
            break
    if not encontrado:
        print("Nenhum animal encontrado!")


def main2():
    while True:
        op = input("\nEscolha uma opção: \n1 - Gerenciar voluntários \n2 - Gerenciar animais \n3 - Sair\n")
        if op == '3':  
            print("Saindo...")
            break
        elif op == '1':  
            while True:
                opcao = input("\nDentre as opções abaixo, o que você deseja fazer? \n1 - Cadastrar um voluntário \n2 - Visualizar informações de um voluntário \n3 - Atualizar informações sobre um voluntário \n4 - Excluir informações sobre um voluntário \n5 - Listar os voluntários existentes \n6 - Voltar ao menu inicial\n")
                match opcao:
                    case "1":
                        while True:
                            print("\n->>> CADASTRAMENTO DE VOLUNTÁRIOS - EM BUSCA DE UM LAR <<<-")
                            nome = input("\nInforme o nome completo do voluntário a ser cadastrado: ")
                            while True:
                                try:
                                    cpf = int(input("n\Informe o CPF do voluntário: "))
                                    break
                                except ValueError:
                                    print("CPF inválido! Digite apenas números.")
                            endereco = input("\nInforme seu bairro")
                            while True:
                                try:
                                    contato = int(input("\nInforme seu melhor contato, apenas em números."))
                                    break
                                except ValueError:
                                    print("Por favor, digite apenas números para o contato.")
                                    
                            while True:
                                horas = input("n\Quantas horas semanais pode dedicar no voluntariado? Digite apenas números.")
                                try:
                                    int(horas)
                                    break
                                except ValueError:
                                    print("Por favor, digite apenas números para as horas.")
                                
                            cadastrar_voluntario(nome, cpf, endereco, contato, horas)
                            maisum = input("Deseja cadastrar mais um voluntário? (s/n): ")
                            if maisum.lower() == 'n':                    
                                break         
                            
                    case "2":
                        while True:
                            nome = input("\nInforme o nome do voluntário a ser procurado: ")
                            buscar_voluntario(nome)
                            maisum = input("Deseja continuar buscando? (s/n): ")
                            if maisum.lower() == 'n':
                                break
                    
                    case "3":
                        while True:
                            nome_antigo = input("Informe o nome completo a ser atualizado (o nome antigo): ")
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
                                    
                            atualizar_voluntario(nome_antigo, novo_nome, novo_ende, novo_contato, novo_horario)
                            maisum = input("Deseja atualizar mais um voluntário? (s/n): ")
                            if maisum.lower() == 'n':
                                break    
                    case "5":
                        listar_voluntario()
                    case "6":
                        print("Voltando ao menu inicial...")
                        break
                    case _:
                        print("Opção inválida! Tente novamente.")
        
        elif op == '2': 
            while True:
                opcao = input("\nDentre as opções abaixo, o que você deseja fazer? \n1 - Cadastrar um animal \n2 - Visualizar informações de um animal \n3 - Atualizar informações sobre um animal \n4 - Excluir informações sobre um animal \n5 - Listar os animais existentes \n6 - Voltar ao menu inicial\n")
                match opcao:
                    case "1":
                        while True:
                            print("\n->>> CADASTRAMENTO DE ANIMAIS - EM BUSCA DE UM LAR <<<-")
                            nome = input("\nInforme o nome do animal a ser cadastrado: ")
                            especie = input("\nInforme a espécie do animal: ")
                            idade = input("\nInforme a idade do animal (em anos): ")
                            porte = input("\nInforme o porte do animal (pequeno, médio e grande): ")
                            raca = input("\nInforme a raça do animal: ")
                            historico_medico = input("\n Fale sobre o animal: É vermifugado? Possui as vacinas em dia? Realizou tratamento ou cirurgia recente? Acrescente o que considerar necessário.): ")
                            cadastrar_animal(nome, especie, idade, porte, raca, historico_medico)
                            maisum = input("Deseja cadastrar mais um animal? (s/n): ")
                            if maisum.lower() == 'n':
                                break
                    case "2":
                        while True:
                            nome = input("\nInforme o nome do animal a ser procurado: ")
                            buscar_animal(nome)
                            maisum = input("Deseja continuar buscando? (s/n): ")
                            if maisum.lower() == 'n':
                                break
                    case "3":
                        while True:
                            nome_antigo = input("Informe o nome do animal a ser atualizado (o nome antigo): ")
                            novo_nome = input("Informe o novo nome: ")
                            nova_especie = input("Informe a nova espécie do animal: ")
                            nova_idade = input("Informe a nova idade do animal: ")
                            historico_medico = input("Informe o novo histórico médico do animal: ")

                            while True:
                                adotado = input("O animal é adotado? (s/n): ").lower()
                                if adotado == 's':
                                        novo_dono = input("Informe o nome completo do dono do animal: ")
                                        break
                                elif adotado == 'n':
                                        novo_dono = None
                                        break
                                else:
                                        print("Opção inválida! Por favor, digite 's' para sim ou 'n' para não.")
                                        continue

                                
                            atualizar_animal(nome_antigo, novo_nome, nova_especie, nova_idade, novo_dono, historico_medico)
                            maisum = input("Deseja atualizar mais um animal? (s/n): ")
                            if maisum.lower() == 'n':
                                break
                            
                    case "4":
                        while True:
                            nome = input("Qual o nome do animal que você deseja excluir? ")
                            excluir_animal(nome)
                            maisum = input("Deseja excluir mais um animal? (s/n): ")
                            if maisum.lower() == 'n':
                                break
                    case "5":
                        listar_animais()
                    case "6":
                        print("Voltando ao menu inicial...")
                        break
                    case _:
                        print("Opção inválida! Tente novamente!")   

if __name__ == "__main__":
    main2()