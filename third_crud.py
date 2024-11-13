import json
import os
import time
from sec_crud import *

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
        if adotante['nome'] == nome:
            print()
            print("\n--- Adotante ---")
            print(f"Nome: {adotante.get('nome')}, ")
            print(f"Idade: {adotante.get('idade')}, ")
            print(f"Bairro: {adotante.get('bairro')}, ")
            print(f"Contato: {adotante.get('contato')}, ")
            print(f"Preferência de porte (1 - Pequeno porte 2 - Médio porte 3 - Grande porte): {adotante.get('preferencia_porte')},")
            print(f"Preferência de especie (1 - Cachorro 2 - Gato 3 - Outro): {adotante.get('preferencia_especie')}")
            return
    print("Nenhum adotante encontrado com esse nome.")

def atualizar_adotante(nome_velho, nome_novo, bairro_escolhido_novo, porte_novo_escolhido, novo_contato_adotante):

    adotantes = carregar_adotantes()

    # Procura o adotante com o nome velho
    for adotante in adotantes:
        if adotante['nome'] == nome_velho:
            # Atualiza os dados do adotante encontrado
            adotante['nome'] = nome_novo
            adotante['bairro'] = bairro_escolhido_novo
            adotante['preferencia_porte'] = porte_novo_escolhido  # Atualizando preferências corretamente
            adotante['contato'] = novo_contato_adotante
            break

    # Salva as alterações de volta no arquivo
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivojson_aberto:
        json.dump(adotantes, arquivojson_aberto, indent=3, ensure_ascii=False)

    print("Adotante atualizado com sucesso!")

    
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
    nome_adotante = input("Informe o nome do adotante para verificar as preferências: ").strip().lower()
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
        especie_animal = str(animal['especie'])  # Convertendo para string para comparação
        porte_animal = str(animal['porte'])

        if preferencia_porte == porte_animal and preferencia_especie == especie_animal:
            print(f"\nEncontrado animal que atende às preferências de {adotante_encontrado['nome']}:")
            print(f"Nome: {animal['nome']}, Espécie: {obter_preferencia_especie(especie_animal)}, Porte: {obter_preferencia_porte(porte_animal)}")
            print("Este animal pode ser uma boa opção para adoção!")
            return animal  

    print("Nenhum animal encontrado que atenda às preferências.")
    return None

def main3():

    while True:

        op = int(input("\nEscolha uma das ações:\n1 - Cadastrar adotante\n2 - Listar adotantes\n3 - Buscar adotante\n4 - Excluir adotante \n5 - Atualizar adotante\n6 - Match \n7 - Voltar para o menu inicial \n8 - Sair da plataforma\nO que deseja fazer? "))

        match op:
            case 1:
                while True:
                    print("---<> CADASTRO DE ADOTANTES NA PLATAFORMA <>---")
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
                print ("--->> LISTA DE ADOTANTES CADASTRADOS NA PLATAFORMA <<---")
                listar_adotantes()

            case 3:
                print ("->-> BUSCAR ADOTANTES NA PLATAFORMA <-<-")   
                nome = input("Informe o nome do adotante para buscar: ")
                buscar_adotante(nome)

            case 4:
                print ("---> EXCLUSÃO DE DADOS DOS ADOTANTES <---")   
                nome = input("Informe o nome do adotante para excluir: ")
                excluir_adotante(nome)

            case 5:
                    
                    print ("\n -->>  ATUALIZAÇÃO DE DADOS DOS ADOTANTE <<--")
                    nome_velho= input ("Informe o nome do adotante que deseja atualizar: ").strip().lower()
                    print("\n -->> ATUALIZAÇÃO DE DADOS DOS ADOTANTES <<--")
                    nome_velho = input("Informe o nome do adotante que deseja atualizar: ").strip().lower()
                    nome_novo = input("Informe o novo nome: ").strip().lower()
                    idade = input("Informe a idade do adotante: ")
                    
                    print("\nBairros disponíveis em Recife:")
                    bairros = ["Boa Viagem", "Casa Forte", "Graças", "Jaqueira", "Torre", "Várzea"]
                    for i, bairro in enumerate(bairros, 1):
                        print(f"{i}. {bairro}")

                    bairro_escolhido_novo = int(input("Escolha o número do bairro desejado: "))

                    if 1 <= bairro_escolhido_novo <= len(bairros):  
                        bairro = bairros[bairro_escolhido_novo - 1]
                        print(f"Bairro escolhido: {bairro}")
                    else:
                        print("Número inválido. Por favor, escolha um número válido de bairro.")

                    contato_novo = input("Informe o contato do adotante: ")



                    print("\nPreferências de animais (porte):")
                    preferencias_porte = ["Pequeno porte", "Médio porte", "Grande porte"]

                    
                    for i, preferencia in enumerate(preferencias_porte, 1):
                        print(f"{i}. {preferencia}")

                    
                    while True:
                        try:
                            porte_novo_escolhido = str(input("Escolha o número da preferência desejada (1-3): "))
                            if 1 <= porte_novo_escolhido and porte_novo_escolhido <= len(preferencias_porte):
                                preferencia_porte = preferencias_porte[porte_novo_escolhido - 1]
                                break
                            else:
                                print("Escolha uma opção válida entre 1 e 3.")
                        except ValueError:
                            print("Entrada inválida. Por favor, insira um número.")

            
                       
                    
                    print("\nPreferências de animais (espécie):")
                    preferencias_especie = ["Cachorro", "Gato", "Outro"]
                    for i, especie in enumerate(preferencias_especie, 1):
                        print(f"{i}. {especie}")


                    preferencia_escolhida_especie = str(input("Escolha o número da preferência de espécie (1-3): "))
                    if 1 <= preferencia_escolhida_especie <= 3:
                        preferencia_especie = preferencias_especie[preferencia_escolhida_especie - 1]
      
                    else:
                        print("Escolha uma opção válida entre 1 e 3.")
    

                    
                    atualizar_adotante(nome_velho, nome_novo, bairro_escolhido_novo, preferencia_porte, contato_novo)


                    print("Dados do adotante atualizados com sucesso!")       

            case 6:
                
                adotantes = carregar_adotantes()  
                animais = carregar_animal()  
                verificar_preferencia_adotante(adotantes, animais) 

            case 7:
                           
                    print(" Voltando para o menu inicial...")
                    break
            case 8:
                print("Saindo do sistema...")
                exit()

            case _:
                    print("Opção inválida! Tente novamente.")

if __name__ == "_main_":
    main3()
