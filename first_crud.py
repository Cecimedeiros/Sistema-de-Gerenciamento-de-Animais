#sistema de gerenciamento da entrada de animais para adoção 
import json
import os
from time import sleep

caminho_arquivo= os.path.join(os.path.dirname(__file__), 'json_abrigo.json')

def carregar_abrigo():
    if not os.path.exists(caminho_arquivo):
        with open (caminho_arquivo,'w') as arquivojson_aberto:
            json.dump([], arquivojson_aberto, indent=3)
    with open (caminho_arquivo, 'r') as arquivojson_aberto:
        return json.load(arquivojson_aberto)

def cadastrar_abrigo (nome, endereco, porte_animal, contato):
    abrigos= carregar_abrigo()
    abrigos.append({'nome': nome, 'endereco': endereco, 'porte_animal': porte_animal,'contato':contato})
    with open (caminho_arquivo, 'w') as arquivojson_aberto:
        json.dump (abrigos, arquivojson_aberto, indent=3, ensure_ascii=False)
    print (" O abrigo foi cadastrado!")

def listar_abrigo():
    abrigos= carregar_abrigo()
    if not abrigos:
        print (" Nenhum abrigo cadastrado! ")
        return
    for abrigo in abrigos:
        print (f" Nome: {abrigo['nome']}, \n Endereço: {abrigo['endereco']},\n Porte do animal: {abrigo['porte_animal']}, Contato: {abrigo['contato']} ")
           
def atualizar_abrigo (nome_antigo, novo_nome, novo_ende, novo_porte_animal, novo_contato):
    abrigos= carregar_abrigo()
    for abrigo in abrigos:
        if abrigo['nome'] == nome_antigo:
            abrigo['nome']=novo_nome
            abrigo['endereco']= novo_ende
            abrigo['porte_animal']= novo_porte_animal
            abrigo['contato']=novo_contato
            break
    with open (caminho_arquivo, 'w') as arquivojson_aberto: 
        json.dump(abrigos, arquivojson_aberto,indent=3, ensure_ascii=False)
    print (" Informações sobre o abrigo atualizadas!")

def excluir_abrigo (nome):
    abrigos=carregar_abrigo()
    for abrigo in abrigos:
        if abrigo['nome']==nome:
            abrigos.remove (abrigo) 
            print (" Dados do abrigo excluídos! ") 
    if not abrigo['nome']==nome:
        print(" Abrigo não existente!")  
    with open (caminho_arquivo, 'w') as arquivojson_aberto:
        json.dump(abrigos, arquivojson_aberto, indent=3, ensure_ascii=False)

def buscar_abrigos(nome):
    abrigos=carregar_abrigo ()
    for abrigo in abrigos:
        if abrigo['nome'] == nome:
            print (f" Nome: {abrigo['nome']},\n Endereço: {abrigo['endereco']},\n Porte do animal: {abrigo['porte_animal']},\n Contato: {abrigo['contato']} ")    
    if not abrigo['nome'] == nome:
        print (" Nenhum abrigo encontrado!")

def main (): 
    print ("\n  <<-------- PLATAFORMA \"EM BUSCA DE UM LAR\" -------->>")
    print ("\n Olá, somos uma plataforma de gerenciamento de animais para adoção!" )
    op= int(input ("\n Aqui você consegue realizar as seguintes ações: \n 1 - Sou um abrigo \n 2 - Sou voluntário(a) da plataforma/Quero me tornar voluntário(a) \n 3 - Quero adotar um animal \n 4 - Sair da plataforma \n O que deseja fazer no momento? "))
  
    if op== 1: 
        opcao=input("\n Dentre as opções abaixo, o que você deseja fazer? \n 1- Cadastrar um abrigo \n 2- Vizualizar informações do abrigo \n 3- Atualizar informações sobre o abrigo \n 4- Excluir informações sobre o abrigo \n 5- Listar os abrigos existentes \n 6- Voltar ao menu inicial ")
        match (opcao):
            case "1": 
                while True:
                    print ("\n ->>> CADASTRAMENTO DE ABRIGOS PARA ANIMAIS <<<-")
                    print ("\n Para cadastrar um novo abrigo é preciso que responda as seguintes perguntas: ")
                    nome=input("\n Informe o nome do abrigo a ser cadastrado: ")
                    endereco= input ("\n Informe a localização do abrigo (bairro, apenas): ")
                    porte_animal= input ("\n Informe o porte dos animais que esse abrigo é capaz de abrigar (pequeno - médio - grande): ")
                    contato=input ("\n Informe o contato do abrigo: ")
                    cadastrar_abrigo(nome, endereco, porte_animal,contato)
                    maisum= input ("Deseja cadastrar mais um abrigo?")
                    if maisum=="n":
                        break
                    
            case "2": 
                while True:
                    print ("\n ->-> BUSCA DE ABRIGOS PARA ANIMAIS <-<-")
                    nome=input("\n Informe o nome do abrigo a ser procurado: ")
                    buscar_abrigos(nome)
                    maisum= input ("Deseja buscar mais um abrigo?")
                    if maisum=="n":
                        break
                    main ()
            case "3":
                while True:
                    print ("\n -->>  ATUALIZAÇÃO DE DADOS DOS ABRIGOS <<--")
                    nome_antigo= input ("Informe o nome a ser atualizado (o nome antigo): ")
                    novo_nome= input ("Informe o novo nome: ")
                    novo_ende= input ("Informe o novo endereço (bairros do estado de Pernambuco) do abrigo: ")
                    novo_porte_animal=input ("Informe o novo tipo de porte de animal que será abrigado pelo abrigo (pequeno - médio - grande): ")
                    novo_contato= input ("Informe o novo contato do abrigo: ")
                    atualizar_abrigo(nome_antigo, novo_nome, novo_ende, novo_porte_animal, novo_contato)
                    maisum= input ("Deseja atualizar mais um abrigo?")
                    if maisum=="n":
                        break       
            case "4":
                while True:
                    print ("\n ------> EXCLUSÃO DE DADOS DOS ABRIGOS PARA ANIMAIS <------")
                    nome= input ("Qual o nome do abrigo você deseja excluir?")
                    excluir_abrigo(nome)
                    maisum= input ("Deseja excluir mais um abrigo?")
                    if maisum=="n":
                        break
                    main ()
            case "5":
                listar_abrigo()
            case "6":
                print ("Voltando ao menu inicial...")
                sleep (4)
                main()  
            case _: 
                print ("Opção inválida! Tente novamente.")
    elif op==2:
        print ("Leo e mel vai fazer")
    elif op==3: 
        print ("Bia e Isa vai fazer ainda")
    elif op==4:  
        print ("Saindo da plataforma. Até logo!")
        fim ()
    else: 
        print ("Opção inválida, tente novamente! ")
        main()
def fim ():
    print ("Saindo da plataforma...")
    
if __name__=="__main__":
    main ()
main ()
fim ()
