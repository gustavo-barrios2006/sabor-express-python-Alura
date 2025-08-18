import os
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

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    match opcao_escolhida:
        case 1:
            print('Cadastrar restaurante')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurantes')
        case 4:
            finalizar_app()
        case _:
            print('Opção inválida!')

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()