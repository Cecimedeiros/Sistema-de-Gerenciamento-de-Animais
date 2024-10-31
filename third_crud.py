import json
import os
from time import sleep

caminho_arquivo = os.path.join(os.path.dirname(__file__), 'adotantes.json')

def carregar_adotantes():
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'w') as arquivojson_aberto:
            json.dump([], arquivojson_aberto, indent=3)
    with open(caminho_arquivo, 'r') as arquivojson_aberto:
        return json.load(arquivojson_aberto)

def cadastrar_adotante(nome, idade, cidade, contato, preferencia_animal):
    adotantes = carregar_adotantes()
    adotantes.append({
        'nome': nome,
        'idade': idade,
        'cidade': cidade,
        'contato': contato,
        'preferencia_animal': preferencia_animal
    })
    with open(caminho_arquivo, 'w') as arquivojson_aberto:
        json.dump(adotantes, arquivojson_aberto, indent=3, ensure_ascii=False)
    print("Adotante cadastrado com sucesso!")

def listar_adotantes():
    adotantes = carregar_adotantes()
    if adotantes:
        for adotante in adotantes:
            nome = adotante.get('nome', 'Nome não disponível')
            idade = adotante.get('idade', 'Idade não disponível')
            cidade = adotante.get('cidade', 'Cidade não disponível')
            contato = adotante.get('contato', 'Contato não disponível')
            preferencia_animal = adotante.get('preferencia_animal', 'Preferência não disponível')
            print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}, Contato: {contato}, Preferência de animal: {preferencia_animal}")
    else:
        print("Nenhum adotante cadastrado!")

def buscar_adotante(nome):
    adotantes = carregar_adotantes()
    encontrado = False
    for adotante in adotantes:
        if adotante['nome'] == nome:
            print(f"Nome: {adotante['nome']}, Idade: {adotante['idade']}, Cidade: {adotante['cidade']}, Contato: {adotante['contato']}, Preferência de animal: {adotante['preferencia_animal']}")
            encontrado = True
            break
    if not encontrado:
        print("Nenhum adotante encontrado com esse nome.")

def excluir_adotante(nome):
    adotantes = carregar_adotantes()
    adotantes_filtrados = [adotante for adotante in adotantes if adotante['nome'] != nome]
    
    if len(adotantes_filtrados) < len(adotantes):
        with open(caminho_arquivo, 'w') as arquivojson_aberto:
            json.dump(adotantes_filtrados, arquivojson_aberto, indent=3, ensure_ascii=False)
        print("Adotante excluído com sucesso!")
    else:
        print("Adotante não encontrado para exclusão.")

# Função principal para gerenciar o sistema
def main():
    print("<<---- PLATAFORMA DE ADOÇÃO ---->>")
    print("Bem-vindo à plataforma de gerenciamento de adotantes!")
    while True:
        op = int(input("\nEscolha uma ação:\n1 - Cadastrar adotante\n2 - Listar adotantes\n3 - Buscar adotante\n4 - Excluir adotante\n5 - Sair\nO que deseja fazer? "))

        if op == 1:
            while True:
                print("---- CADASTRO DE ADOTANTE ----")
                nome = input("Informe o nome do adotante: ")
                idade = input("Informe a idade do adotante: ")
                
                # Escolha de cidade
                print("\nCidades disponíveis em Recife:")
                cidades = ["Boa Viagem", "Casa Forte", "Graças", "Jaqueira", "Torre", "Várzea"]
                for i, cidade in enumerate(cidades, 1):
                    print(f"{i}. {cidade}")
                cidade_escolhida = int(input("Escolha o número da cidade desejada: "))
                cidade = cidades[cidade_escolhida - 1]
                
                contato = input("Informe o contato do adotante: ")

                # Escolha de preferência de animal
                print("\nPreferências de animais:")
                preferencias = ["Cachorro", "Gato", "Pássaro", "Outros"]
                for i, preferencia in enumerate(preferencias, 1):
                    print(f"{i}. {preferencia}")
                preferencia_escolhida = int(input("Escolha o número da preferência desejada: "))
                preferencia_animal = preferencias[preferencia_escolhida - 1]

                cadastrar_adotante(nome, idade, cidade, contato, preferencia_animal)

                maisum = input("Deseja cadastrar mais um adotante? (s/n): ").strip().lower()
                if maisum == 'n':
                    break

        elif op == 2:
            listar_adotantes()

        elif op == 3:
            nome = input("Informe o nome do adotante para buscar: ")
            buscar_adotante(nome)

        elif op == 4:
            nome = input("Informe o nome do adotante para excluir: ")
            excluir_adotante(nome)

        elif op == 5:
            print("Saindo da plataforma. Até logo!")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
