from dados import eventos

    
def adicionar():
    nome_evento = input('\n:Qual o nome do evento que deseja adicionar? ')
    print(f'O evento "\n{nome_evento}" foi adicionado. ')
    
    

        
escolhas = { 
"add": adicionar, 
"remove": remover, 
"list": listar,
"quit": sair, 
            }