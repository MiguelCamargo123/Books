class Livro:
    def __init__(self, nome, genero, autor, data):
        self.nome = nome
        self.genero = genero
        self.autor = autor
        self.data = data

    def __str__(self):
        return f'{self.nome} - {self.genero} - {self.autor} - ({self.data})'

biblioteca = []

def registarLivro():
    nome = input('Nome do livro: ')
    genero = input('Genero do livro: ')
    autor = input('Autor do livro: ')
    anoPublicado = int(input('Ano de publicação: '))

    livro = Livro(nome, genero, autor, anoPublicado)

    biblioteca.append(livro)

def verLivros():
    print('Atualmente temos os seguintes livros: ')
    for i, livros in enumerate(biblioteca, start=1):
        print(f'-{i} {livros}')

pergunta = input('Você deseja entrar em nossa biblioteca? (S/N) ').upper()

while pergunta == 'S':
    print()
    oqueFazer = input('Você deseja [R]egistrar um livro, [V]er os livros? ').upper()

    if oqueFazer == 'R':
        try:
            print()
            registarLivro()
            print('Livro registrado com sucesso!')
        except ValueError:
            print()
            print('Por favor, digite um ano, não um texto')

    if oqueFazer == 'V':
        print()
        verLivros()