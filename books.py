import json


class Livro:
    def __init__(self, nome, genero, autor, data):
        self.nome = nome
        self.genero = genero
        self.autor = autor
        self.data = data

    def __str__(self):
        return f'{self.nome} - {self.genero} - {self.autor} - ({self.data})'


class Biblioteca:
    def __init__(self):
        self.disponiveis = []
        self.emprestados = []
        self._carregar_json()

    def _carregar_json(self):
        try:
            with open('biblioteca.json', 'r', encoding='utf-8') as f:
                dados = json.load(f)
                for d in dados:
                    livro = Livro(
                        d['nome'], d['genero'], d['autor'], d['ano de publicação']
                    )
                    self.disponiveis.append(livro)
        except FileNotFoundError:
            pass

        try:
            with open('emprestados.json', 'r', encoding='utf-8') as f:
                dados_emprestimo = json.load(f)
                for d in dados_emprestimo:
                    livro_emprestimo = Livro(
                        d['nome'], d['genero'], d['autor'], d['ano de publicação']
                    )
                    self.emprestados.append(livro_emprestimo)
        except FileNotFoundError:
            pass

    def _salvar_json(self):
        with open('biblioteca.json', 'w', encoding='utf-8') as f:
            json.dump(
                [
                    {
                        'nome': l.nome,
                        'genero': l.genero,
                        'autor': l.autor,
                        'ano de publicação': l.data,
                    }
                    for l in self.disponiveis
                ],
                f,
                ensure_ascii=False,
                indent=4,
            )

        with open('emprestados.json', 'w', encoding='utf-8') as f:
            json.dump(
                [
                    {
                        'nome': l.nome,
                        'genero': l.genero,
                        'autor': l.autor,
                        'ano de publicação': l.data,
                    }
                    for l in self.emprestados
                ],
                f,
                ensure_ascii=False,
                indent=4,
            )

    def registarLivro(self, nome, genero, autor, anoPublicado):
        livro = Livro(nome, genero, autor, anoPublicado)
        self.disponiveis.append(livro)
        self._salvar_json()

    def verLivros(self):
        print('Atualmente temos os seguintes livros: ')
        for i, livros in enumerate(self.disponiveis, start=0):
            print(f'indice: -{i} {livros}')

    def emprestar(self, indice):
        if range(len(self.disponiveis)) > 0:
            if indice in range(len(self.disponiveis)):
                if len(self.emprestados) < 3:
                    livro = self.disponiveis.pop(indice)
                    self.emprestados.append(livro)
                    print('Livro emprestado com sucesso!')
                    self._salvar_json()
                else:
                    print(
                        'Você tem três livros emprestados, devolva um e você poderá pegar outro'
                    )
        else:
            print(
                'Você não registrou nenhum livro para emprestar ainda, tente registrar um!!'
            )

    def livrosEmprestados(self):
        print('Atualmente você pegou os seguintes livros emprestados: ')
        for i, emprestado in enumerate(self.emprestados):
            print(f'indice: -{i} {emprestado}')

    def devolverLivro(self, indice):
        if range(len(self.emprestados)) > 0:
            if indice in range(len(self.emprestados)):
                devolvido = self.emprestados.pop(indice)
                self.disponiveis.append(devolvido)
                print('Livro devolvido com sucesso!')
                self._salvar_json()
            else:
                print('Índice inválido!')
        else:
            print(
                'Você não pegou nenhum livro emprestdo ainda, tente pegar um primeiro'
            )

    def removerLivro(self, indice):
        if range(len(self.disponiveis)) > 0:
            if indice in range(len(self.disponiveis)):
                self.disponiveis.pop(indice)
                print('Livro removido com sucesso!!')
                self._salvar_json()
            else:
                print(
                    'Digite um indice valido, se você não sabe digite V para ver os livros e os indices'
                )
        else:
            print(
                'Ainda não tem livros disponiveis para remover, tente adicionar um antes!!!'
            )


def main():
    biblioteca = Biblioteca()

    while True:
        oque_fazer = input(
            'Você deseja [R]egistrar um livro? [V]er os livros disponiveis? [E]mprestar um livro? [Q]auis livros você pegou emprestado? [D]evolver um livro? '
        ).upper()

        if oque_fazer == 'R':
            nome = input('Digite o nome do livro: ')
            genero = input('Digite o genero do livro: ')
            autor = input('Digite o nome do autor do livro: ')
            anoPublicado = int(input('Digite o ano de publicação do livro: '))

            try:
                biblioteca.registarLivro(nome, genero, autor, anoPublicado)
                print('Livro registrado com sucesso')
            except ValueError:
                print('Digite o ano de publicação, não um texto!!!')

        elif oque_fazer == 'V':
            biblioteca.verLivros()

        elif oque_fazer == 'E':
            indice = int(
                input('Digite o indice do livro que deseja pegar emprestado: ')
            )
            try:
                biblioteca.emprestar(indice)
            except ValueError:
                print(
                    'Digite o indice do livro que deseja pegar emprestado, não um texto!!!'
                )

        elif oque_fazer == 'Q':
            biblioteca.livrosEmprestados()

        elif oque_fazer == 'D':
            indice2 = int(input('Digite o indice do livro que voce deseja devolver: '))
            try:
                biblioteca.devolverLivro(indice2)
            except ValueError:
                print('Digite um indice, não um texto!!!')

        print()
        pergunta = input('Você deseja continuar? (S/N) ').upper()
        if pergunta != 'S':
            break


if __name__ == '__main__':
    main()
