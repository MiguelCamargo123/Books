class Livro:
    def __init__(self, nome, genero, autor, data):
        self.nome = nome
        self.genero = genero
        self.autor = autor
        self.data = data

    def __str__(self):
        return f'{self.nome} - {self.genero} - {self.autor} - ({self.data})'

biblioteca = []
emprestados = []

def registarLivro():
    nome = input('Nome do livro: ')
    genero = input('Genero do livro: ')
    autor = input('Autor do livro: ')
    anoPublicado = int(input('Ano de publicação: '))

    livro = Livro(nome, genero, autor, anoPublicado)

    biblioteca.append(livro)

def verLivros():
    print('Atualmente temos os seguintes livros: ')
    for i, livros in enumerate(biblioteca, start=0):
        print(f'indice: -{i} {livros}')

def emprestar(indice):
    if indice in range(len(biblioteca)):
        if len(emprestados) < 3:
            livro = biblioteca.pop(indice)
            emprestados.append(livro)
            print('Livro emprestado com sucesso!')
        else:
            print('Você tem três livros emprestados, devolva um e você podera pegar outro')

def livrosEmprestados():
    print('Atualmente você pegou os seguintes livros emprestados: ')
    for i, emprestado in enumerate(emprestados):
        print(f'indice: -{i} {emprestado}')

pergunta = input('Você deseja entrar em nossa biblioteca? (S/N) ').upper()

while pergunta == 'S':
    print()
    oqueFazer = input('Você deseja [R]egistrar um livro, [V]er os livros, [P]egar emprestado um livro, [S]aber quantos livros foram pegos emprestado? ').upper()

    if oqueFazer == 'R':
        try:
            print()
            registarLivro()
            print('Livro registrado com sucesso!')
            print()
        except ValueError:
            print()
            print('Por favor, digite um ano, não um texto')
            print()

    if oqueFazer == 'V':
        print()
        verLivros()
        print()

    if oqueFazer == 'P':
        print()
        emprestimo = int(input('Digite o indice do livro: '))
        emprestar(emprestimo)

    if oqueFazer == 'P':
        print()
        livrosEmprestados()