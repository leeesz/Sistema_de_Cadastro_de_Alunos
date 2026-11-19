import psycopg

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "sistema_alunos",
    "user": "postgres",
    "password": "123456",
}


def conectar():
    return psycopg.connect(**DB_CONFIG)


def criar_tabela():
    with conectar() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS alunos (
                    id SERIAL PRIMARY KEY,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    nota REAL NOT NULL
                )
            """)
        conn.commit()


def adicionar_aluno():
    nome = input("\nNome do aluno: ").strip()

    while True:
        try:
            idade = int(input("Idade do aluno: "))
            break
        except ValueError:
            print("Idade inválida! Digite um número inteiro.")

    while True:
        try:
            nota = float(input("Nota do aluno (0 a 10): "))
            if 0 <= nota <= 10:
                break
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Nota inválida! Digite um número.")

    with conectar() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO alunos (nome, idade, nota) VALUES (%s, %s, %s)",
                (nome, idade, nota),
            )
        conn.commit()

    print(f"\nAluno {nome} salvo no banco de dados.")
    input("\nAperte ENTER para voltar ao menu principal...")


def listar_alunos():
    with conectar() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nome, idade, nota FROM alunos ORDER BY id")
            registros = cursor.fetchall()

    if not registros:
        print("\nNenhum aluno cadastrado ainda.\n")
    else:
        print("\n--- LISTA DE ALUNOS ---")
        for _, nome, idade, nota in registros:
            print(f"Nome: {nome} | Idade: {idade} | Nota: {nota}")
        print("------------------------\n")

    input("Aperte ENTER para voltar ao menu principal...")


def buscar_aluno():
    nome_busca = input("\nDigite o nome do aluno que deseja buscar: ").strip()

    with conectar() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT nome, idade, nota FROM alunos WHERE LOWER(nome) = LOWER(%s)",
                (nome_busca,),
            )
            aluno = cursor.fetchone()

    if aluno:
        nome, idade, nota = aluno
        print(f"\nAluno {nome} encontrado. Idade: {idade} | Nota: {nota}")
    else:
        print(f"\nO aluno {nome_busca} não está cadastrado.")

    input("\nAperte ENTER para voltar ao menu principal...")


def remover_aluno():
    nome_remover = input("\nDigite o nome do aluno que deseja remover: ").strip()

    with conectar() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM alunos WHERE LOWER(nome) = LOWER(%s)",
                (nome_remover,),
            )
            removidos = cursor.rowcount
        conn.commit()

    if removidos > 0:
        print(f"\nAluno {nome_remover} removido com sucesso.")
    else:
        print(f"\nO aluno {nome_remover} não foi encontrado para ser removido.")

    input("\nAperte ENTER para voltar ao menu principal...")


def mostrar_media():
    with conectar() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT AVG(nota) FROM alunos")
            media = cursor.fetchone()[0]

    if media is None:
        print("\nNão há notas cadastradas para calcular a média.")
    else:
        print(f"\nMédia geral das notas: {float(media):.2f}")

    input("\nAperte ENTER para voltar ao menu principal...")


def exibir_menu():
    print("""
            MENU PRINCIPAL        
        1 - Adicionar aluno
        2 - Listar todos os alunos
        3 - Buscar aluno pelo nome
        4 - Remover aluno
        5 - Mostrar média geral das notas
        6 - Sair
    """)


def menu():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1 a 6): ").strip()

        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno()
        elif opcao == "4":
            remover_aluno()
        elif opcao == "5":
            mostrar_media()
        elif opcao == "6":
            print("\nSaindo do sistema... Até logo!\n")
            break
        else:
            print("\nOpção inválida, tente novamente")


if __name__ == "__main__":
    criar_tabela()
    menu()