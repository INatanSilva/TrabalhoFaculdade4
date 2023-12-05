# Mensagem de boas-vindas
print("Bem-vindo ao Sistema de Gerenciamento de Livros do Natan Dos Santos Silva")
print('*' *73)

# Lista vazia
lista_livro = []

# Variável global
id_global = 0

# Cadastro do livro
def cadastrar_livro(id):
    print('*' *73)
    print('-' * 26, 'MENU CADASTRAR LIVRO', '-' *25)
    print('ID do livro: {}'.format(id))
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")

    livro = {
        "id": id_global,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }

    lista_livro.append(livro)

# Consulta ao livro
def consultar_livro():
    print('*' *73)
    print('-' *30, 'MENU CONSULTAR LIVRO', '-' *29)
    opcao = input("Escolha uma opção:\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Autor\n4. Retornar ao menu\n")

    if opcao == "1":
        for livro in lista_livro:
            print(livro)
    elif opcao == "2":
        id_consulta = int(input("Digite o Id do livro a ser consultado: "))
        for livro in lista_livro:
            if livro["id"] == id_consulta:
                print(livro)
    elif opcao == "3":
        autor_consulta = input("Digite o nome do autor a ser consultado: ")
        for livro in lista_livro:
            if livro["autor"] == autor_consulta:
                print(livro)
    elif opcao == "4":
        return
    else:
        print("Opção inválida")

# Remover livro
def remover_livro():
    id_remover = int(input("Digite o Id do livro a ser removido: "))
    for livro in lista_livro:
        if livro["id"] == id_remover:
            lista_livro.remove(livro)
            print(f"Livro com Id {id_remover} removido com sucesso.")

# Menu
def main():
    global id_global  
    while True:
        print('-' * 28, 'MENU PRINCIPAL', '-' *29)
        opcao_menu = input("Escolha uma opção desejada:\n1. Cadastrar Livro\n2. Consultar Livro\n3. Remover Livro\n4. Encerrar Programa\n")

        if opcao_menu == "1":
            id_global += 1
            cadastrar_livro(id_global)
        elif opcao_menu == "2":
            consultar_livro()
        elif opcao_menu == "3":
            remover_livro()
        elif opcao_menu == "4":
            print("Encerrando o programa. Obrigado!")
            break
        else:
            print("Opção inválida")

# Chamar a função main para iniciar o programa
main()