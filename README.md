# 📚 Library Management System

A CLI-based Library Management System built with Python.

This project was developed to practice:

- Object-Oriented Programming (OOP)
- Code structure and organization
- Input validation
- Clean logic implementation
- Structural Pattern Matching (`match` statements)
- NoSQL data persistence (JSON)

## 🚀 Features

- Add books to the library
- List available books
- Lend books to users
- Track borrowed books
- Return borrowed books
- Remove books from the library
- Name-based validation for all operations
- Data persistence with JSON — all data is saved and restored between sessions

## 🛠️ Technologies

- Python 3.10+
- JSON (built-in)

## ▶️ How to Run

1. Clone the repository:

```bash
git clone git@github.com:MiguelCamargo123/Books.git
```

2. Navigate into the project folder:

```bash
cd Books
```

3. Run the application:

```bash
python books.py
```

## 📦 Version

### v1.2.0 (current)

- Added book removal functionality (removerLivro)

- Refactored validation logic for lending, returning, and removing books to search by name instead of index

- Replaced list .pop() operations with .remove() for better object handling

- Replaced if/elif menu with match statement (Python 3.10+)

- Improved input validation messages

### v1.1.0

- Added full data persistence using JSON files (biblioteca.json and emprestados.json)

- Refactored save logic into a single \_salvar_json() helper method

- Fixed devolverLivro not updating JSON on return

- Code cleanup and deduplication

### v1.0.0

- First complete and stable implementation of the system

- OOP structure with Livro and Biblioteca classes

- CLI menu with input validation

## 📄 License

_This project is licensed under the MIT License._
