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
    except json.JSONDecodeError:
        return {}


def salvar_filmes(filmes):
    with open(ARQUIVO_FILMES, "w", encoding="utf-8") as arquivo:
        json.dump(filmes, arquivo, indent=4, ensure_ascii=False)


def quer_continuar(mensagem):
    resposta = input(mensagem).strip().lower()
    return resposta == "s"


def cadastrar_filme(filmes):
    while True:
        limpar_tela()
        print("=== Cadastrar filme ===")

        nome = input("Digite o nome do filme: ").strip()
        if not nome:
            print("O nome do filme nao pode ficar vazio.")
            input("Pressione ENTER para continuar...")
            continue

        ano = input("Digite o ano do filme: ").strip()
        diretor = input("Digite o diretor do filme: ").strip()
        genero = input("Digite o genero do filme: ").strip()
        atores_texto = input("Digite os atores separados por virgula: ").strip()
        atores = [ator.strip() for ator in atores_texto.split(",") if ator.strip()]

        filmes[nome] = {
            "ano": ano,
            "diretor": diretor,
            "genero": genero,
            "atores": atores
        }

        salvar_filmes(filmes)
        print("Filme adicionado com sucesso!")

        if not quer_continuar("Deseja cadastrar outro filme? (s/n): "):
            break


def excluir_filme(filmes):
    while True:
        limpar_tela()
        print("=== Excluir filme ===")

        if not filmes:
            print("Nenhum filme inserido.")
            input("Pressione ENTER para continuar...")
            return

        listar_filmes(filmes, pausar=False)
        nome = input("\nDigite o nome do filme a deletar: ").strip()

        if nome in filmes:
            del filmes[nome]
            salvar_filmes(filmes)
            print("Filme deletado com sucesso!")
        else:
            print("Filme nao encontrado.")

        if not quer_continuar("Deseja deletar outro filme? (s/n): "):
            break


def listar_filmes(filmes, pausar=True):
    if filmes:
        print("\nFilmes inseridos:")
        for nome, info in filmes.items():
            ano = info.get("ano", info.get("data", "Nao informado"))
            diretor = info.get("diretor", "Nao informado")
            genero = info.get("genero", "Nao informado")
            atores = ", ".join(info.get("atores", [])) or "Nao informado"

            print(f"\nNome: {nome}")
            print(f"Ano: {ano}")
            print(f"Diretor: {diretor}")
            print(f"Genero: {genero}")
            print(f"Atores: {atores}")
    else:
        print("Nenhum filme inserido.")

    if pausar:
        input("Pressione ENTER para continuar...")


def menu():
    print("\nMenu:")
    print("1 - Inserir filme")
    print("2 - Deletar filme")
    print("3 - Listar filmes")
    print("4 - Sair")


def main():
    filmes_usuario = carregar_filmes()

    while True:
        limpar_tela()
        menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_filme(filmes_usuario)
        elif opcao == "2":
            excluir_filme(filmes_usuario)
        elif opcao == "3":
            limpar_tela()
            listar_filmes(filmes_usuario)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opcao invalida. Tente novamente.")
            input("Pressione ENTER para continuar...")


if __name__ == "__main__":
    main()
