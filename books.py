class Livros:
    def __init__(self, autor, nomeLivro,  genero, anoPublicação):
        self.autor = autor
        self.nome = nomeLivro
        self.genero = genero
        self.anoPublicação = anoPublicação
        self.__livrosDentro = []

    def registrarLivro(self):
        self.__livrosDentro.append([autor, nome, genero, ano_publicacao])
        print('Livro registrado com sucesso')

autor = input('Digite o nome do autor: ')
nome = input('Digite o nome do livro: ')
genero = input('Digite o genero do livro: ')
ano_publicacao = int(input('Digite o ano de publicação: '))

livro = Livros(autor, nome, genero, ano_publicacao)
livro.registrarLivro()
