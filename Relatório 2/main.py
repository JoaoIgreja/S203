from filme import Filme
from catalogo import CatalogoFilmes


def main():
    catalogo = CatalogoFilmes()

    while True:
        print("\n1. Adicionar Filme")
        print("2. Listar Filmes")
        print("3. Buscar por Ano")
        print("4. Buscar por Genero")
        print("5. Buscar por Diretor")
        print("6. Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            titulo = input("Titulo: ")
            ano = int(input("Ano de Lancamento: "))
            diretor = input("Diretor(a): ")
            genero = input("Genero: ")
            duracao = input("Duracao (minutos): ")
            filme = Filme(titulo, ano, diretor, genero, duracao)
            catalogo.adicionar_filme(filme)
            print("Filme adicionado com sucesso!")

        elif opcao == "2":
            print("\nFilmes no Catalogo:")
            for filme in catalogo.listar_filmes():
                print(filme)

        elif opcao == "3":
            ano = int(input("Digite o ano de lancamento: "))
            filmes = catalogo.buscar_por_ano(ano)
            if filmes:
                print(f"\nFilmes lancados em {ano}:")
                for filme in filmes:
                    print(filme)
            else:
                print("Nenhum filme encontrado para o ano especificado.")

        elif opcao == "4":
            genero = input("Digite o genero: ")
            filmes = catalogo.buscar_por_genero(genero)
            if filmes:
                print(f"\nFilmes do genero {genero}:")
                for filme in filmes:
                    print(filme)
            else:
                print("Nenhum filme encontrado para o genero especificado.")

        elif opcao == "5":
            diretor = input("Digite o diretor: ")
            filmes = catalogo.buscar_por_diretor(diretor)
            if filmes:
                print(f"\nFilmes dirigidos por {diretor}:")
                for filme in filmes:
                    print(filme)
            else:
                print("Nenhum filme encontrado para o diretor especificado.")

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opcao invalida. Por favor, escolha novamente.")


if __name__ == "__main__":
    main()
