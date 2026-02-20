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
    for i, livros in enumerate(biblioteca, start=0):
        print(f'indice: -{i} {livros}')

def emprestar(indice):
    if indice in range(len(biblioteca)):
        biblioteca.pop(indice)
        print('Livro emprestado com sucesso!')

pergunta = input('Você deseja entrar em nossa biblioteca? (S/N) ').upper()

while pergunta == 'S':
    print()
    oqueFazer = input('Você deseja [R]egistrar um livro, [V]er os livros, [E]mprestar um livro? ').upper()

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

    if oqueFazer == 'E':
        print()
        emprestimo = int(input('Digite o indice do livro: '))
        emprestar(emprestimo)
        print('livro emprestado com sucesso')