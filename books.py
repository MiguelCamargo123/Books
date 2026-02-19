class Livros:
    def __init__(self, autor, genero, anoPublicação):
        self.autor = autor
        self.genero = genero
        self.anoPublicação = anoPublicação

autor = input('Digite o nome do autor: ')
genero = input('Digite o genero do livro: ')
ano_publicacao = int(input('Digite o ano de publicação: '))

livro = Livros(autor, genero, ano_publicacao)
