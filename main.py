from util import limpar_tela
import menu
import funções
from menu import escolha_user

from menu import exibir_menu

def main():
    
    while True:
        escolha_user = exibir_menu(escolha_user)
        if escolha_user == 0:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()