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

def devolverLivro(indice):
    if indice in range(len(emprestados)):
        devolvido = emprestados.pop(indice)
        biblioteca.append(devolvido)
        print('Livro devolvido com sucesso!')
    else:
        print('Índice inválido!')


def main():
    while True:
        pergunta = input('Você deseja sair de nosso sistema? (S/N) ').upper()

        if pergunta == 'S':
            break

        print()
        desejaFazer = input('Você deseja [R]egistrar um livro, [V]er os livros, [E]mprestar um livro, [O]lhar quais livros emprestados ou [D]evolver um livro?').upper()

        if desejaFazer == 'R':
            print()
            try:
                registarLivro()
                print('livro registrado com sucesso!')
            except ValueError:
                print('Digite o ano de publicação do livro, não um texto')

        elif desejaFazer == 'V':
            print()
            verLivros()
        
        elif desejaFazer == 'E':
            print()
            try:
                emprestimo = int(input('Digite o indice do livro que você deseja pegar emprestado: '))
                emprestar(emprestimo)
            except ValueError:
                print('Digite o indice do livro, não um texto')

        elif desejaFazer == 'O':
            print()
            livrosEmprestados()
        
        elif desejaFazer == 'D':
            print()
            try:
                indiceDevolver = int(input('Digite o indice do livro que você deseja devolver: '))
                devolverLivro(indiceDevolver)
            except ValueError:
                print('Digite o indice do livro, não um texto')

        pergunta = input('Você deseja continuar? (S/N) ').upper()
        if pergunta != 'S':
            break


if __name__ == '__main__':
    main()