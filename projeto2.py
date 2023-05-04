print('\n --- Um Porsche é tão individual quanto o seu proprietário.---\n\n SEJA BEM VINDO A PORSCHE, A MARCA MAIS DESEJADA DO AUTOMOBILISMO.\n' )
nome= input('Como deseja ser chamado? ')
email= input('\nDigite seu e-mail: ')
tel= input('\nDigite seu telefone: ')
def menu():
    while True:
        print ('\n1- Carros ')
        print ('2- Mecânica')
        print ('3- Atendimento')
        print ('4-sair')
        opcao= input('\nDigite um número para a opção que desejar: ')

        if opcao == '1':
            menu_de_carros()
        elif opcao == '2':
            mecanica()
        elif opcao == '3':
            atendimento()
        else:
            break

def menu_de_carros():
    print ('\n1- Porche 911')
    print ('2- Panamera')
    print ('3- Macan')
    print ('4- 718\n')
    escolhe_carro= input('Digite um número para o opção do carro que deseja: ')
    
    if escolhe_carro == '1':
        opcionais_do_carro()
    elif escolhe_carro == '2':
        opcionais_do_carro()    
    elif escolhe_carro == '3':
        opcionais_do_carro() 
    elif escolhe_carro == '4':
        opcionais_do_carro()    
    else:
        return 




def opcionais_do_carro():  # Início da parte estética co carro
     
    menu_de_cores()

    

def menu_de_cores():
    print('\nAgora vamos escolher a cor externa de seu carro')
    
    print ('\n1- Vermelho')
    print ('2- Azul')
    print ('3- Amarelo')
    print ('4- Retorna ao menu inicial\n')
    
    escolhe_cor= input('Digite um número para o opção que desejar: ')
    
    if escolhe_cor == '1':
        print('\nOK A cor externa do seu carro será vermelha\n')
        menu_de_rodas()
    elif escolhe_cor == '2':
        print('\nOK A cor externa do seu carro será azul\n')
        menu_de_rodas()
    elif escolhe_cor == '3':
        print('\nOK A cor externa do seu carro será amarelo\n')
        menu_de_rodas()
    else:
        return

def menu_de_rodas():
    
    print('Agora vamos escolher as rodas de seu carro\n')
    
    print ('1- Aro 20')
    print ('2- Aro 21')
    print ('3- Aro 22')
    print ('4- Retorna ao menu inicial\n')
    
    escolhe_rodas= input('Digite um número para o opção que desejar: ')
   
    if escolhe_rodas == '1':
        print('OK A cor das rodas de seu carro serão de aro 20\n')
        menu_do_interior()
    elif escolhe_rodas == '2':
        print('OK A cor das rodas de seu carro serão de aro 21\n')
        menu_do_interior()
    elif escolhe_rodas == '3':
        print(' OK A cor das rodas de seu carro serão de aro 22\n')
        menu_do_interior()
    else:
        return
    
    

def menu_do_interior():
    print('Agora vamos escolher a cor do interior de seu carro')
    print('\n')
    print ('1- Caramelo')
    print ('2- Preto')
    print ('3- Branco')
    print ('4- Retorna ao menu inicial\n')
    
    escolhe_interior= input('Digite um número para o opção que desejar: ')
    print('\n')
    if escolhe_interior == '1':
         print('Seu carro terá interior caramelo\n\n\n')
         mensagem()    
    elif escolhe_interior == '2':
        print('Seu carro terá interior preto\n\n\n')
        mensagem()
    elif escolhe_interior == '3':
        print(' Seu carro teraá interior branco\n\n\n')
        mensagem()
    else:
        return
    
    
def mensagem():
    print (nome,'\nAgradecemos o seu contato.\nAnotamos todas as suas preferências e entraremos em contato em breve.\n')
    print('Digite a opção desejada: ')


# Menu de Mecânica

def mecanica():
    print ('1-Motor')
    print ('2-Freio e suspensão')
    print ('3-troca de óleo')
    print ('4- retorna')
    print ('5-sair')

    opcao3= input(' digite um número para o opção que desejar')

    if opcao3 == '1':
        menumotor()
    elif opcao3 == '2':
        freio_suspensao()
    elif opcao3 == '3':
        print ('opção C')
    elif opcao3 == '4':
        menu()
    else:
        return

# Início da parte de motor

def menumotor():
    print('mensagem inicial para o cliente')
    print ('1-embreagem')
    print ('2-câmbio')
    print ('3-cabeçote')
    print ('4-sair')
    
    opcao= input('digite um número para o opção que desejar: ')


    if opcao == '1':
        print('Certo, já temos seus dados. Vamos entrar em contato')
    elif opcao == '2':
        print('Certo, já temos seus dados. Vamos entrar em contato')
    elif opcao == '3':
        print('Certo, já temos seus dados. Vamos entrar em contato')
    else:
        return

# freio e suspensão

def freio_suspensao():
    print('mensagem inicial para o cliente')
    print ('1- Pastilhas de Freio')
    print ('2- óleo da suspensão')
    print ('3- Discos')
    print ('4-sair')
    
    opcao= input('digite um número para o opção que desejar: ')


    if opcao == '1':
        print('Certo, já temos seus dados. Vamos entrar em contato')
    elif opcao == '2':
        print('Certo, já temos seus dados. Vamos entrar em contato')
    elif opcao == '3':
        print('Certo, já temos seus dados. Vamos entrar em contato')
    else:
        return
    
    # Troca de óleo

def troca_de_oleo():
    print('mensagem inicial para o cliente')
    print ('1- Óleo de motor')
    print ('2- Óleo de câmbio')
    print ('3- Óleo de freio')
    print ('4-sair')
    
    opcao= input('digite um número para o opção que desejar: ')


    if opcao == '1':
        print('Certo, já temos seus dados. Vamos entrar em contato')
    elif opcao == '2':
        print('Certo, já temos seus dados. Vamos entrar em contato')
    elif opcao == '3':
        print('Certo, já temos seus dados. Vamos entrar em contato')
    else:
        return



# Atendimento


def atendimento():
    print ('1-Recepção')
    print ('2-Peças')
    print ('3-ShowRoom')
    print ('4- retorna')
    print ('5-sair')

    opcao4= input(' digite um número para o opção que desejar')

    if opcao4 == '1':
        print ('Alguma coisa sobre Recepção')
    elif opcao4 == '2':
        print('Alguma coisa sobre Peças')
    elif opcao4 == '3':
        print ('Alguma coisa sobre showRoom')
    elif opcao4 == '4':
        menu()
    else:
        return


def reiniciar():
    opcao = input("Deseja fazer outra pergunta? (s/n)")

    if opcao.lower() == "s":
        menu()
    else:
        print("Obrigado por utilizar nosso bot de atendimento!")
        return


menu()