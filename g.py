alunos = [] 

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
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Nota inválida! Digite um número.")
    
    aluno = {"nome": nome, "idade": idade, "nota": nota}
    alunos.append(aluno)
    
    print(f"\n✅ Aluno {nome} cadastrado com sucesso!")
    input("\nAperte ENTER para voltar ao menu principal...")

def listar_alunos():
    if not alunos:
        print("\n❌ Nenhum aluno cadastrado ainda.\n")
    else:
        print("\n--- LISTA DE ALUNOS ---")
        for aluno in alunos:
            print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']}")
        print("------------------------\n")
        
    input("Aperte ENTER para voltar ao menu principal...")

def buscar_aluno():
    nome_busca = input("\nDigite o nome do aluno que deseja buscar: ").strip()
    encontrado = False

    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca.lower():
            print(f"\n✅ O aluno {aluno['nome']} foi encontrado no sistema! Idade: {aluno['idade']} | Nota: {aluno['nota']}")
            encontrado = True
            break
            
    if not encontrado:
        print(f"\n❌ O aluno {nome_busca} não está cadastrado.")
        
    input("\nAperte ENTER para voltar ao menu principal...")
    
def remover_aluno():
    nome_remover = input("\nDigite o nome do aluno que deseja remover: ").strip()
    encontrado = False

    for aluno in alunos:
        if aluno["nome"].lower() == nome_remover.lower():
            alunos.remove(aluno)
            print(f"\n✅ O aluno {aluno['nome']} foi removido com sucesso!")
            encontrado = True
            break
            
    if not encontrado:
        print(f"\n❌ O aluno {nome_remover} não foi encontrado para ser removido.")
        
    input("\nAperte ENTER para voltar ao menu principal...")

def mostrar_media():
    print("\n--- MÉDIA GERAL (em construção) ---")
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

menu()