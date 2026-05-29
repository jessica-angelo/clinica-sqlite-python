import sqlite3


# 🔧 CRIA A TABELA
def criar_tabela():
    conexao = sqlite3.connect("clinica.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
    """)

    conexao.commit()
    conexao.close()


# ➕ CADASTRAR PACIENTE
def cadastrar_paciente():
    nome = input("Nome do paciente: ")
    idade = int(input("Idade do paciente: "))

    conexao = sqlite3.connect("clinica.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO pacientes (nome, idade) VALUES (?, ?)",
        (nome, idade)
    )

    conexao.commit()
    conexao.close()

    print("\nPaciente cadastrado com sucesso!")


# 📋 LISTAR PACIENTES
def listar_pacientes():
    conexao = sqlite3.connect("clinica.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, idade FROM pacientes")
    pacientes = cursor.fetchall()

    conexao.close()

    print("\n=== LISTA DE PACIENTES ===")

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return

    for p in pacientes:
        print("----------------")
        print("ID:", p[0])
        print("Nome:", p[1])
        print("Idade:", p[2])


# ✏️ EDITAR PACIENTE
def editar_paciente():
    id_paciente = int(input("ID do paciente que deseja editar: "))
    novo_nome = input("Novo nome: ")
    nova_idade = int(input("Nova idade: "))

    conexao = sqlite3.connect("clinica.db")
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE pacientes
        SET nome = ?, idade = ?
        WHERE id = ?
    """, (novo_nome, nova_idade, id_paciente))

    conexao.commit()
    conexao.close()

    print("\nPaciente atualizado com sucesso!")


# 🗑️ DELETAR PACIENTE
def deletar_paciente():
    id_paciente = int(input("ID do paciente que deseja deletar: "))

    conexao = sqlite3.connect("clinica.db")
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM pacientes
        WHERE id = ?
    """, (id_paciente,))

    conexao.commit()
    conexao.close()

    print("\nPaciente deletado com sucesso!")


# 📋 MENU
def menu():
    print("\n=== MENU ===")
    print("1 - Cadastrar paciente")
    print("2 - Listar pacientes")
    print("3 - Editar paciente")
    print("4 - Deletar paciente")
    print("5 - Sair")


# 🚀 INICIALIZA BANCO
criar_tabela()

print("Banco criado com sucesso!")

# 🔁 LOOP PRINCIPAL
while True:
    menu()
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_paciente()

    elif opcao == "2":
        listar_pacientes()

    elif opcao == "3":
        editar_paciente()

    elif opcao == "4":
        deletar_paciente()

    elif opcao == "5":
        print("Sistema encerrado")
        break

    else:
        print("Opção inválida")