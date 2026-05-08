import json
import os


ARQUIVO_FILMES = "filmes.json"


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def carregar_filmes():
    if not os.path.exists(ARQUIVO_FILMES):
        return {}

    try:
        with open(ARQUIVO_FILMES, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def salvar_filmes(filmes):
    with open(ARQUIVO_FILMES, "w", encoding="utf-8") as arquivo:
        json.dump(filmes, arquivo, indent=4, ensure_ascii=False)


def perguntar_continuar(mensagem):
    resposta = input(mensagem).strip().lower()
    return resposta == "s"


def cadastrar_filme(filmes):
    while True:
        limpar_tela()
        print("=== Cadastrar filme ===")

        titulo = input("Digite o titulo do filme: ").strip()
        if not titulo:
            print("O titulo nao pode ficar vazio.")
            input("Pressione ENTER para continuar...")
            continue

        ano = input("Digite o ano do filme: ").strip()
        diretor = input("Digite o diretor do filme: ").strip()
        genero = input("Digite o genero do filme: ").strip()
        atores_texto = input("Digite os atores separados por virgula: ").strip()

        atores = []
        if atores_texto:
            atores = [ator.strip() for ator in atores_texto.split(",") if ator.strip()]

        filmes[titulo] = {
            "ano": ano,
            "diretor": diretor,
            "genero": genero,
            "atores": atores
        }

        salvar_filmes(filmes)
        print("\nFilme cadastrado com sucesso!")

        if not perguntar_continuar("Deseja cadastrar outro filme? (s/n): "):
            break


def excluir_filme(filmes):
    while True:
        limpar_tela()
        print("=== Excluir filme ===")

        if not filmes:
            print("Nenhum filme cadastrado.")
            input("Pressione ENTER para continuar...")
            return

        listar_filmes(filmes, pausar=False)
        titulo = input("\nDigite o titulo do filme que deseja excluir: ").strip()

        if titulo in filmes:
            del filmes[titulo]
            salvar_filmes(filmes)
            print("Filme excluido com sucesso!")
        else:
            print("Filme nao encontrado.")

        if not perguntar_continuar("Deseja excluir outro filme? (s/n): "):
            break


def listar_filmes(filmes, pausar=True):
    print("=== Lista de filmes ===")

    if not filmes:
        print("Nenhum filme cadastrado.")
    else:
        for titulo, dados in filmes.items():
            atores = ", ".join(dados.get("atores", [])) or "Nao informado"
            print(f"\nTitulo: {titulo}")
            print(f"Ano: {dados.get('ano', 'Nao informado')}")
            print(f"Diretor: {dados.get('diretor', 'Nao informado')}")
            print(f"Genero: {dados.get('genero', 'Nao informado')}")
            print(f"Atores: {atores}")

    if pausar:
        input("\nPressione ENTER para continuar...")


def menu():
    print("\n=== Menu de filmes ===")
    print("1 - Cadastrar filme")
    print("2 - Excluir filme")
    print("3 - Listar filmes")
    print("4 - Sair")


def main():
    filmes = carregar_filmes()

    while True:
        limpar_tela()
        menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_filme(filmes)
        elif opcao == "2":
            excluir_filme(filmes)
        elif opcao == "3":
            limpar_tela()
            listar_filmes(filmes)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opcao invalida. Tente novamente.")
            input("Pressione ENTER para continuar...")


if __name__ == "__main__":
    main()
