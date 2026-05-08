import os

FilmesUsuario = {}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("\nMenu:")
    print("1 - Inserir filme")
    print("2 - Deletar filme")
    print("3 - Listar filmes")
    print("4 - Sair")

while True:
    limpar_tela()
    menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        nome = input("Digite o nome do filme: ")
        data_lancamento = input("Digite a data de lançamento: ")
        genero = input("Digite o gênero do filme: ")
        FilmesUsuario[nome] = {'data': data_lancamento, 'genero': genero}
        print("Filme adicionado com sucesso!")
        input("Pressione ENTER para continuar...")
    
    elif opcao == '2':
        nome = input("Digite o nome do filme a deletar: ")
        if nome in FilmesUsuario:
            del FilmesUsuario[nome]
            print("Filme deletado com sucesso!")
        else:
            print("Filme não encontrado.")
        input("Pressione ENTER para continuar...")
    
    elif opcao == '3':
        if FilmesUsuario:
            print("\nFilmes inseridos:")
            for nome, info in FilmesUsuario.items():
                print(f"Nome: {nome}, Data: {info['data']}, Gênero: {info['genero']}")
        else:
            print("Nenhum filme inserido.")
        input("Pressione ENTER para continuar...")
    
    elif opcao == '4':
        print("Saindo...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
        input("Pressione ENTER para continuar...")