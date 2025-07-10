import sqlite3
from datetime import datetime

# Conexão com o banco (cria se não existir)
conexao = sqlite3.connect("biblioteca.db")

# Criar um cursor
cursor = conexao.cursor()

# Criar a tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    autor TEXT,
    categoria TEXT,
    isbn TEXT
)
''')
cursor.execute(
'''CREATE TABLE IF NOT EXISTS emprestimos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_livro INTEGER,
    nome_usuario TEXT,
    data_emprestimo TEXT,
    data_devolucao TEXT,
    devolvido INTEGER DEFAULT 0,
    FOREIGN KEY (id_livro) REFERENCES livros(id)
)''')


# Salva e fecha a conexão inicial
conexao.commit()

# cadastrar livros caso a opção for 1
def cadastrar_livro():
        titulo = input ("Digite o titulo do livro: ")
        autor = input('Digite o autor: ')
        categoria =  input('Digite a categoria (ex: Romance, Ficção, Infantil):')
        ISBN =  input('Digite a ISBN: ')

        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("INSERT INTO livros (titulo, autor, categoria, ISBN) VALUES (?, ?, ?, ?)",
                   (titulo, autor, categoria, ISBN))

        conexao.commit()
        conexao.close()
        print("Livro cadastrado com sucesso!")

# pesquisar caso a opção for 2, usa o lower para os caracteres fiquem todos minusculos para analise
def pesquisar_livro():
        pesq = (input ("Digite o titulo ou autor do livro: ")).lower()
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""SELECT titulo, autor, categoria, ISBN FROM livros WHERE LOWER(titulo) LIKE ? OR LOWE (autor) LIKE ?""", (f"%{pesq}%", f"%{pesq}%"))

        resultados = cursor.fetchall()
        conexao.close()

        if resultados:
            print(f"Foram encontrados {len(resultados)} livro(s):")
            for l in resultados:
                print(f"Título: {l[0]}, Autor: {l[1]}, Categoria: {l[2]}, ISBN: {l[3]}")
        else:
            print("Nenhum livro encontrado com esse título ou autor.")

# consutar emprestimo e devolução caso a opção for 3            
def emprestimo_livro() :
    titulo = (input ("Digite o titulo do livro que deseje realizar o emprestimo: ")).lower()
    nome_usuario = input("Digite o nome da pessoa que está pegando o livro: ")
    data_emprestimo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    # Verificar se o livro já está emprestado
    cursor.execute("SELECT id FROM livros WHERE LOWER(titulo) = ?", (titulo,))
    resultado = cursor.fetchone()

    if resultado is None:
        print("Livro não encontrado.")
        conexao.close()
        return

    id_livro = resultado[0]

    # Verifica se o livro já está emprestado
    cursor.execute("SELECT * FROM emprestimos WHERE id_livro = ? AND devolvido = 0", (id_livro,))
    emprestado = cursor.fetchone()

    if emprestado:
        print("Este livro já está emprestado.")
    else:
        cursor.execute('''
            INSERT INTO emprestimos (id_livro, nome_usuario, data_emprestimo)
            VALUES (?, ?, ?)
        ''', (id_livro, nome_usuario, data_emprestimo))
        conexao.commit()
        print("Empréstimo registrado com sucesso!")
   
    conexao.close()

def listar_emprestimo():    
# Listar todos os emprestimos
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT l.titulo, e.nome_usuario, e.data_emprestimo
        FROM emprestimos e
        JOIN livros l ON e.id_livro = l.id
        WHERE e.devolvido = 0
    ''')

    emprestimos = cursor.fetchall()
    conexao.close()
    if emprestimos:
        print("\n Livros atualmente emprestados:")
        for titulo, usuario, data in emprestimos:
            print(f"- '{titulo}' emprestado para {usuario} em {data}")
    else:
        print("\nNenhum livro emprestado no momento.")
   
def devolucao_livro():
    titulo = input("Digite o título do livro a ser devolvido: ").strip().lower()
    data_devolucao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    # Buscar o livro pelo título
    cursor.execute("SELECT id FROM livros WHERE LOWER(titulo) = ?", (titulo,))
    resultado = cursor.fetchone()

    if resultado is None:
        print("Livro não encontrado.")
        conexao.close()
        return

    id_livro = resultado[0]

    # Atualizar empréstimo
    cursor.execute('''
        UPDATE emprestimos
        SET devolvido = 1,
            data_devolucao = ?
        WHERE id_livro = ? AND devolvido = 0
    ''', (data_devolucao, id_livro))

    if cursor.rowcount == 0:
        print("Nenhum empréstimo ativo encontrado para esse livro.")
    else:
        conexao.commit()
        print("Livro devolvido com sucesso!")
   
    conexao.close()

def listar_dev():
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT l.titulo, e.nome_usuario, e.data_emprestimo, e.data_devolucao
        FROM emprestimos e
        JOIN livros l ON e.id_livro = l.id
        WHERE e.devolvido = 1
    ''')

    devolvidos = cursor.fetchall()
    conexao.close()

    if devolvidos:
        print("\n Livros devolvidos:")
        for titulo, usuario, emprestimo, devolucao in devolvidos:
            print(f"- '{titulo}' foi emprestado para {usuario} em {emprestimo} e devolvido em {devolucao}")
    else:
        print("\nNenhum livro devolvido ainda.")



while True:
        print("\nESCOLHA UMA DAS OPÇÕES:")
        print("1 - Cadastrar livros")
        print("2 - Pesquisar livro por título ou autor")
        print("3 - Realizar emprestimos")
        print("4 - Realizar devoluções")
        print("5 - Listar emprestimos")
        print("6 - Listar devoluções")
        print("7 - Sair")
        try:
            op = int(input("Opção: "))
        except:
            print("Digite um número válido.")
            continue

        if op == 1:
            cadastrar_livro()
        elif op == 2:
            pesquisar_livro()
        elif op == 3:
            emprestimo_livro()
        elif op == 4:
            devolucao_livro()
        elif op == 5:
            listar_emprestimo()
        elif op == 6:
            listar_dev()
        elif op == 7:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

