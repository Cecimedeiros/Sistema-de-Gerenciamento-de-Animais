import json
import os
from time import sleep
from crud_voluntarios_animais import *

caminho_arquivo = os.path.join(os.path.dirname(__file__), 'adotantes.json')

def carregar_adotantes():
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'w',  encoding='utf-8') as arquivojson_aberto:
            json.dump([], arquivojson_aberto, indent=3)


    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivojson_aberto:
        return json.load(arquivojson_aberto)

def cadastrar_adotante(nome, idade, bairro, contato, preferencia_porte, preferencia_especie):
    adotantes = carregar_adotantes()
    adotantes.append({
        'nome': nome,
        'idade': idade,
        'bairro': bairro,
        'contato': contato,
        'preferencia_especie':preferencia_especie,
        'preferencia_porte': preferencia_porte,
    })
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivojson_aberto:
        json.dump(adotantes, arquivojson_aberto, indent=3, ensure_ascii=False)
    print("Adotante cadastrado com sucesso!")

def listar_adotantes():
    adotantes = carregar_adotantes()
    if adotantes:
        for adotante in adotantes:
            print("\n--- Adotante ---")
            print(f"Nome: {adotante.get('nome', 'Não disponível')}")
            print(f"Idade: {adotante.get('idade', 'Não disponível')}")
            print(f"Bairro: {adotante.get('bairro', 'Não disponível')}")
            print(f"Contato: {adotante.get('contato', 'Não disponível')}")
            print(f"Preferência de porte (1 - Pequeno porte 2 - Médio porte 3 - Grande porte): {adotante.get('preferencia_porte', 'Não disponível')}")
            print(f"Preferência de espécie (1 - Cachorro 2 - Gato 3 - Outro): {adotante.get('preferencia_especie', 'Não disponível')}")
            print()  
    else:
        print("Nenhum adotante cadastrado!")

def buscar_adotante(nome):
    adotantes = carregar_adotantes()  

    for adotante in adotantes:

        if adotante['nome'].strip().lower() == nome.strip().lower():
            print("\n--- Adotante Encontrado ---")
            print(f"Nome: {adotante.get('nome')}")
            print(f"Idade: {adotante.get('idade')}")
            print(f"Bairro: {adotante.get('bairro')}")
            print(f"Contato: {adotante.get('contato')}")
            print(f"Preferência de porte (1 - Pequeno porte, 2 - Médio porte, 3 - Grande porte): {adotante.get('preferencia_porte')}")
            print(f"Preferência de espécie (1 - Cachorro, 2 - Gato, 3 - Outro): {adotante.get('preferencia_especie')}")
            return

    print("Nenhum adotante encontrado com esse nome.")

def atualizar_adotante(nome_velho, nome_novo, idade, bairro, preferencia_porte, preferencia_especie, contato_novo):
    try:
        with open('adotantes.json', 'r') as f:
            adotantes = json.load(f)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
        return

    for adotante in adotantes:
        if adotante['nome'].lower() == nome_velho.lower():
            adotante['nome'] = nome_novo
            adotante['idade'] = idade
            adotante['bairro'] = bairro
            adotante['preferencia_porte'] = preferencia_porte  
            adotante['preferencia_especie'] = preferencia_especie 
            adotante['contato'] = contato_novo
           
            with open('adotantes.json', 'w') as f:
                json.dump(adotantes, f, indent=4)
            print(f"Adotante {nome_velho} atualizado com sucesso.")
            return

    print("Adotante não encontrado.")

    
def excluir_adotante(nome):
    adotantes = carregar_adotantes()
    adotantes_filtrados = [adotante for adotante in adotantes if adotante['nome'] != nome]
    
    if len(adotantes_filtrados) < len(adotantes):
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivojson_aberto:
            json.dump(adotantes_filtrados, arquivojson_aberto, indent=3, ensure_ascii=False)
        print("Adotante excluído com sucesso!")
    else:
        print("Adotante não encontrado para exclusão.")


def obter_preferencia_especie(numero):
    especie_map = {
        "1": "Cachorro",
        "2": "Gato",
        "3": "Outro",
    }
    return especie_map.get(numero.strip(), "")

def obter_preferencia_porte(numero):
    porte_map = {
        "1": "Pequeno porte",
        "2": "Médio porte",
        "3": "Grande porte"
    }
    return porte_map.get(numero.strip(), "")

def verificar_preferencia_adotante(adotantes, animais):
    nome_adotante = input("\nInforme o nome do adotante para verificar as preferências: ").strip().lower()
    adotante_encontrado = None

    for adotante in adotantes:
        if adotante['nome'].strip().lower() == nome_adotante:
            adotante_encontrado = adotante
            break    

    if not adotante_encontrado:
        print("Adotante não encontrado.")
        return None

    print(f"Verificando preferências de adoção para {adotante_encontrado['nome']}...")

    preferencia_especie = adotante_encontrado['preferencia_especie']
    preferencia_porte = adotante_encontrado['preferencia_porte']

    for animal in animais:
        especie_animal = str(animal['especie']) 
        porte_animal = str(animal['porte'])

        if preferencia_porte == porte_animal and preferencia_especie == especie_animal:
            print(f"\nEncontrado animal que atende às preferências de {adotante_encontrado['nome']}:")
            print(f"Nome: {animal['nome']}, Espécie: {obter_preferencia_especie(especie_animal)}, Porte: {obter_preferencia_porte(porte_animal)}")
            print("Este animal pode ser uma boa opção para adoção! ;) \nAdemais, caso queira saber mais sobre o animal, vá até o menu secundário e escolha a opção \"Listar animais disponíveis para adoção\"")
            return animal  

    print("Nenhum animal encontrado que atenda às preferências. Se quiser saber mais sobre outros animais, vá até o menu secundário e escolha \"Listar animais disponíveis para adoção\"")

def main3():

    while True:

        op = int(input("\nEscolha uma das ações:\n1 - Cadastrar adotante\n2 - Listar adotantes\n3 - Buscar adotante\n4 - Excluir adotante \n5 - Atualizar adotante\n6 - Match \n7 - Listar animais disponíveis para adoção \n8 - Voltar para o menu inicial \n9 - Sair da plataforma\nO que deseja fazer? "))

        match op:
            case 1:
                while True:
                    print("\n---<> CADASTRO DE ADOTANTES NA PLATAFORMA - EM BUSCA DE UM LAR <>---")
                    nome = input("Informe o nome do adotante: ")

                  
                    while True:
                        try:
                            idade = int(input("Informe a idade do adotante: "))
                            if idade <= 0:
                                print("A idade deve ser maior que 0. Tente novamente.")
                            else:
                                break
                        except ValueError:
                            print("Entrada inválida. Por favor, insira um número válido para a idade.")

                   
                    print("\nBairros disponíveis em Recife:")
                    bairros = ["Boa Viagem", "Casa Forte", "Graças", "Jaqueira", "Torre", "Várzea"]
                    for i, bairro in enumerate(bairros, 1):
                        print(f"{i}. {bairro}")

             
                    while True:
                        try:
                            bairro_escolhido = int(input("Escolha o número do bairro desejado: "))
                            if 1 <= bairro_escolhido <= len(bairros):
                                bairro = bairros[bairro_escolhido - 1]
                                break
                            else:
                                print("Escolha um número válido do menu.")
                        except ValueError:
                            print("Entrada inválida. Por favor, insira um número válido.")

                    contato = input("Informe o contato do adotante: ")
                                        
                    print("\nEscolha a preferência de porte do animal:")
                    preferencias_porte = ["Pequeno porte", "Médio porte", "Grande porte"]
                    for i, preferencia in enumerate(preferencias_porte, 1):
                        print(f"{i}. {preferencia}")

                    while True:
                        try:
                            preferencia_escolhida_porte = int(input("Escolha o número da preferência de porte: "))
                            if 1 <= preferencia_escolhida_porte <= len(preferencias_porte):
                                preferencia_porte = str(preferencia_escolhida_porte)  
                                break
                            else:
                                print("Escolha uma opção válida do menu.")
                        except ValueError:
                            print("Entrada inválida. Por favor, insira um número válido.")

                   
                    print("\nEscolha a preferência de espécie do animal:")
                    preferencias_especie = ["Cachorro", "Gato", "Outro"]
                    for i, especie in enumerate(preferencias_especie, 1):
                        print(f"{i}. {especie}")

                    while True:
                        try:
                            preferencia_escolhida_especie = int(input("Escolha o número da preferência de espécie: "))
                            if 1 <= preferencia_escolhida_especie <= len(preferencias_especie):
                                preferencia_especie = str(preferencia_escolhida_especie)  
                                break
                            else:
                                print("Escolha uma opção válida do menu.")
                        except ValueError:
                            print("Entrada inválida. Por favor, insira um número válido.")
                    cadastrar_adotante(nome, idade, bairro, contato, preferencia_especie, preferencia_porte)

                    
                    maisum = input("\nDeseja cadastrar mais um adotante? (s/n): ").strip().lower()
                    if maisum == 'n':
                        break

            case 2:
                print ("\n--->> LISTA DE ADOTANTES CADASTRADOS NA PLATAFORMA - EM BUSCA DE UM LAR <<---")
                listar_adotantes()

            case 3:
                print ("\n->-> BUSCAR ADOTANTES NA PLATAFORMA - EM BUSCA DE UM LAR <-<-")   
                nome = input("Informe o nome do adotante para buscar: ")
                buscar_adotante(nome)

            case 4:
                print ("\n---> EXCLUSÃO DE DADOS DOS ADOTANTES - EM BUSCA DE UM LAR <---")   
                nome = input("Informe o nome do adotante para excluir: ")
                excluir_adotante(nome)

            case 5:
                    
                print("\n -->>  ATUALIZAÇÃO DE DADOS DOS ADOTANTES - EM BUSCA DE UM LAR <<--")
                nome_velho = input("Informe o nome do adotante que deseja atualizar: ").strip().lower()
                nome_novo = input("Informe o novo nome: ").strip().lower()

                idade_valida = False
                while not idade_valida:
                    idade = input("Informe a idade do adotante: ")
                    try:
                        idade = int(idade)  
                        idade_valida = True
                    except ValueError:
                        print("Por favor, insira uma idade válida (somente números).")

                print("\nBairros disponíveis em Recife:")
                bairros = ["Boa Viagem", "Casa Forte", "Graças", "Jaqueira", "Torre", "Várzea"]
                for i, bairro in enumerate(bairros, 1):
                    print(f"{i}. {bairro}")

                bairro_valido = False
                while not bairro_valido:
                    try:
                        bairro_escolhido_novo = int(input("Escolha o número do bairro desejado: "))
                        if 1 <= bairro_escolhido_novo <= len(bairros):
                            bairro = bairros[bairro_escolhido_novo - 1]
                            bairro_valido = True
                            print(f"Bairro escolhido: {bairro}")
                        else:
                            print("Número inválido. Por favor, escolha um número válido de bairro.")
                    except ValueError:
                        print("Entrada inválida. Por favor, insira um número.")

                print("\nPreferências de animais (porte):")
                preferencias_porte = ["Pequeno porte", "Médio porte", "Grande porte"]
                for i, preferencia in enumerate(preferencias_porte, 1):
                    print(f"{i}. {preferencia}")

                porte_valido = False
                while not porte_valido:
                    try:
                        porte_novo_escolhido = int(input("Escolha o número da preferência desejada (1-3): "))
                        if 1 <= porte_novo_escolhido <= len(preferencias_porte):
                            preferencia_porte = porte_novo_escolhido  
                            porte_valido = True
                        else:
                            print("Escolha uma opção válida entre 1 e 3.")
                    except ValueError:
                        print("Entrada inválida. Por favor, insira um número.")

                print("\nPreferências de animais (espécie):")
                preferencias_especie = ["Cachorro", "Gato", "Outro"]
                for i, especie in enumerate(preferencias_especie, 1):
                    print(f"{i}. {especie}")

                especie_valida = False
                while not especie_valida:
                    try:
                        preferencia_escolhida_especie = int(input("Escolha o número da preferência de espécie (1-3): "))
                        if 1 <= preferencia_escolhida_especie <= len(preferencias_especie):
                            preferencia_especie = preferencia_escolhida_especie  
                            especie_valida = True
                        else:
                            print("Escolha uma opção válida entre 1 e 3.")
                    except ValueError:
                        print("Entrada inválida. Por favor, insira um número.")

                contato_novo = input("Informe o contato do adotante: ")

                atualizar_adotante(nome_velho, nome_novo, idade, bairro, preferencia_porte, preferencia_especie, contato_novo)

                print("Dados do adotante atualizados com sucesso!")


            case 6:
                
                adotantes = carregar_adotantes()  
                animais = carregar_animal()  
                verificar_preferencia_adotante(adotantes, animais) 
            case 7:
                print("\n->>> LISTA DE DADOS DE ANIMAIS - EM BUSCA DE UM LAR <<<-")   
                listar_animal()
            case 8:              
                print("\nVoltando para o menu inicial...")
                break
            case 9:
                print("Saindo do sistema...")
                exit()

            case _:
                    print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main3()
