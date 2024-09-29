#simulação de uma TV com opções de ação

def menu_tv():
    opcao = "" #inicializa as variáveis/listas
    op = []
    c = ""
    listaCanais = programarCanais()

    while opcao != "2": #se 2 for o primeiro número a ser entrado, o programa será encerrado
        print("Menu:")
        print("1 - Ligar Tv")
        print("2 - Desligar Tv")
        print("3 - Trocar/escolher canal")
        print("4 - Exibir canal atual")

        opcao = input("Escolha uma opção: ")
        op.append(opcao)
        #print("op = ", op) #para conferir qual número foi dado como entrada

        if op[0] != '1':
            print("Primeiro, ligue a TV.")
            op.pop() #tira da lista o número no índice 0 que for diferente de 1, pois a condição é de, antes de tudo, ligar a TV
        else:
            if opcao == "1":
                print("TV ligada. Programando canais...")
                print("Finalizado. Sua televisão possui ", len(listaCanais), " canais para utilizar.")
            elif opcao == "2":
                print("Televisão desligada.")
            elif opcao == "3":
                c = int(input("Qual canal você deseja acessar?\n"))
                c -= 1
                print("Canal ",listaCanais[c]," acessado.")
            elif opcao == "4":
                if c == '':
                    print("Antes, escolha um canal.")
                else:
                    print("Você está no canal ", listaCanais[c],".")
            else:
                print("Opção desconhecida")

def programarCanais():
    canais = [
        {"Canal 1": "Desenhos"},
        {"Canal 2": "Filmes"},
        {"Canal 3": "Séries"},
        {"Canal 4": "Documentários"},
        {"Canal 5": "Esportes"},
        {"Canal 6": "Notícias"},
        {"Canal 7": "Variedades"},
        {"Canal 8": "Música"},
        {"Canal 9": "Infantil"},
        {"Canal 10": "Religião"}
    ]
    return canais

menu_tv()
