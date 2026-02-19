class Biblioteca:
    def __init__(self, autor, nomeLivro, genero, anoPublicacao):
        self.autor = autor
        self.nomeLivro = nomeLivro
        self.genero = genero
        self.anoPublicacao = anoPublicacao
        self.__quantidadeLivros = []

    def registrarLivro(self, autor, nomeLivro, genero, anoPublicacao):
        livro = {
            'nome': nomeLivro,
            'genero': genero,
            'autor': autor,
            'anoPublicacao': anoPublicacao
        }
        self.__quantidadeLivros.append(livro)

