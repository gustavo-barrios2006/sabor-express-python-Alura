import os
restaurantes = ['Pizza', 'Sushi']
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu')
    main()

def finalizar_app():
    os.system('cls')
    print('Encerrando o programa\n')

def exibir_nome_do_programa():
    print('ˢᵃᵇᵒʳ ᴱˣᵖʳᵉˢˢ\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()
    
def cadastrar_novo_restaurante():
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    print('Listando os restaurantes\n')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    voltar_ao_menu_principal()
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurantes')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()