# 📚 Sistema de Biblioteca em Python + SQLite

Este projeto é um sistema simples de gerenciamento de uma **biblioteca**, desenvolvido em **Python** utilizando o banco de dados **SQLite**. Ele permite:

- Cadastro de livros com título, autor, categoria e ISBN
- Pesquisa de livros por título ou autor
- Registro de empréstimos e devoluções
- Listagem de livros emprestados e devolvidos

---

## 🛠 Requisitos

Antes de executar o sistema, verifique se você possui:

- Python 3.7 ou superior instalado
- Biblioteca padrão do Python (`sqlite3`, `datetime`) — já incluídas por padrão

---

## 💻 Como executar o projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/sofia-azeved0/senac-1-coding-av2
   ```

2. **Acesse o diretório do projeto:**

   ```bash
   cd senac-1-coding-av2
   ```

3. **Execute o programa:**

   ```bash
   python biblioteca.py
   ```

---

## 📋 Funcionalidades

Ao rodar o sistema, você verá o seguinte menu:

```
ESCOLHA UMA DAS OPÇÕES:
1 - Cadastrar livros
2 - Pesquisar livro por título ou autor
3 - Realizar empréstimos
4 - Realizar devoluções
5 - Listar empréstimos
6 - Listar devoluções
7 - Sair
```

### 📌 Descrição:

- **Cadastrar livros**: Insere livros no banco com título, autor, categoria e ISBN.
- **Pesquisar**: Busca livros por título ou autor (sem diferenciação de maiúsculas/minúsculas).
- **Empréstimos**: Registra o empréstimo de um livro para um usuário.
- **Devoluções**: Marca um livro como devolvido e registra a data.
- **Listar empréstimos**: Mostra livros que estão atualmente emprestados.
- **Listar devoluções**: Exibe histórico de devoluções.

---

## 🧱 Estrutura do Banco

São utilizadas duas tabelas:

- `livros`: Armazena os dados dos livros.
- `emprestimos`: Registra os empréstimos, devoluções e quem pegou o livro.

---

## 📁 Licença

Este projeto é de uso educacional. Sinta-se livre para modificar e reutilizar.

---

Desenvolvido como parte de um projeto escolar em 14/07/2025 ✨
