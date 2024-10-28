#sistema de gerenciamento da entrada de animais para adoção (perfil dos animais)
import json

def inicio (): 
    print (" <<-------- PLATAFORMA EM BUSCA DE UM LAR -------->>")
    print ("\n Olá, somos uma plataforma de gerenciamento de animais para adoção!" )
    op= int(input ("\n Aqui você consegue realizar as seguintes ações: \n 1- Adotar um animal \n 2 - Ser voluntário da plataforma \n 3- cadastrar um abrigo de animal \n 4- Sair da plataforma \n O que deseja fazer no momento? "))
    
    if op== 1: 
        questionario ()
    elif op==2:
        voluntario ()
    elif op==3: 
        abrigo ()
    elif op==4:  
        print ("Saindo da plataforma. Até logo!")
        fim ()
    else: 
        print ("Opção inválida, tente novamente! ")
        inicio()
               
def questionario ():
  
    while True:
        respostas = {}

        print ("\n ------> SISTEMA DE GERENCIAMENTO DA ENTRADA DE ANIMAIS PARA ADOÇÃO <------")
        print ("\n Por favor, responda as seguintes perguntas sobre o animal a ser cadastrado: ")
        
        nome= input("\n Informe o nome do animal: ")
        animal= input("\n Informe qual tipo de animal está entrando para o processo de adoção:  ")
        sexo=input("\n Informe o sexo do animal: ")
        idade=int(input("\n Informe a idade do animal (apenas anos): "))
        raca=input("\n Informe a raça do animal: ")
        porte= input ("\n Informe o porte do animal (pequeno, médio ou grande): ")
        personalidade=input("\n Diga 3 adjetivos que descreva a personalidade do animalzinho: ")
        historico_medico= input("\n Informe mais detalhes sobre o histórico médico do animal: ")
        necessidades= input(f"\n Informe 3 necessidades do(a) {nome} observadas (ex: casa grande, outro cachorro presente, ração pedigree): ")
        foto= input("\n Para finalizar o cadastro, encaminhe uma foto do animal: \n")
        #falta permitir entrar a foto
        
        respostas[nome]= animal, sexo, idade, raca, personalidade, historico_medico, necessidades, foto, porte

        print (respostas)

        opcao= input ("\n Deseja continuar cadastrando algum outro animal (sim ou não)? ")
        
        if opcao=="não" or opcao=='n' or opcao=="nn":
            print ("\n O animal foi cadastrado no sistema de adoção, esperamos que, em breve, possa achar um bom lar!")
            break
    inicio()

def voluntario ():
    
    while True:
        info_voluntarios = {}

        print ("------> SISTEMA DE GERENCIAMENTO DE VOLUNTÁRIOS <------")   
        print ("Que alegria ver você aqui! Para se tornar um(a) voluntário (a) da Plataforma precisamos de algumas informações." "\n Por favor, preencha-as.")
            
        nome= input("\n Informe o nome completo do(a) voluntário(a): ")
        cpf= input("Informe seu CPF (sem pontos e hífens, ex: 19181028909): ")
        endereco= input ("Informe a cidade e o estado em que vive: ")
        horas= input ("Informe a quantidade de horas semanais que pode trabalhar na plataforma: ")

        info_voluntarios[cpf]=nome, endereco, horas
        print(info_voluntarios)

        opcao= input("Deseja cadastrar mais algum(a) voluntário(a) (sim ou não)?")
        if opcao=="não" or opcao=="nn":
            print ("Cadastro finalizado! Seja bem vindo(a)!")
            break
    inicio ()
    
def abrigo ():
    
    while True:
        info_abrigo= {}
        print ("------> SISTEMA DE GERENCIAMENTO DO CADASTRAMENTO DE ABRIGOS PARA ANIMAIS <------")
        print ("\n Para cadastrar um novo abrigo é preciso que responda as seguintes perguntas: ")

        nome=input("\n Informe o nome do abrigo a ser cadastrado: ")
        endereco= input ("\n Informe a localização do abrigo (cidade e estado, apenas): ")
        tipo_animal= input ("\nInforme o porte dos animais que esse abrigo é capaz de abrigar: ")
        contato=input ("\n Informe o contato do abrigo: ")

        info_abrigo [nome]= endereco, tipo_animal, contato
        print (info_abrigo)

        opcao= input ("Abrigo cadastrado com sucesso! Deseja cadastrar mais algum abrigo (sim ou não)? ")
        if opcao=="não" or opcao=="nn":
            print ("\n Voltando para o menu.")
            break
    inicio ()

def fim ():
    print ("Obrigada! Até mais")
        
def main (): 
    inicio ()

main ()
