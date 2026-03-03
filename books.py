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

    def registarLivro(self):
        nome = input('Nome do livro: ')
        genero = input('Genero do livro: ')
        autor = input('Autor do livro: ')
        anoPublicado = int(input('Ano de publicação: '))

        livro = Livro(nome, genero, autor, anoPublicado)

        self.disponiveis.append(livro)
        livros_nosDisponiveis = [
            {
                'nome': livro.nome,
                'genero': livro.genero,
                'autor': livro.autor,
                'ano de publicação': anoPublicado,
            }
            for l in self.disponiveis
        ]

        with open('biblioteca.json', 'w', encoding='utf-8') as f:
            json.dump(livros_nosDisponiveis, f, ensure_ascii=False, indent=4)

    def verLivros(self):
        print('Atualmente temos os seguintes livros: ')
        for i, livros in enumerate(self.disponiveis, start=0):
            print(f'indice: -{i} {livros}')

    def emprestar(self, indice):
        if indice in range(len(self.disponiveis)):
            if len(self.emprestados) < 3:
                livro = self.disponiveis.pop(indice)
                self.emprestados.append(livro)
                print('Livro emprestado com sucesso!')

                # Salva lista de emprestados no JSON
                livros_nosEmprestados = [
                    {
                        'nome': l.nome,
                        'genero': l.genero,
                        'autor': l.autor,
                        'ano de publicação': l.data,
                    }
                    for l in self.emprestados
                ]
                with open('emprestados.json', 'w', encoding='utf-8') as f:
                    json.dump(livros_nosEmprestados, f, ensure_ascii=False, indent=4)

                # Atualiza o JSON de disponíveis também (livro saiu da lista!)
                livros_nosDisponiveis = [
                    {
                        'nome': l.nome,
                        'genero': l.genero,
                        'autor': l.autor,
                        'ano de publicação': l.data,
                    }
                    for l in self.disponiveis
                ]
                with open('biblioteca.json', 'w', encoding='utf-8') as f:
                    json.dump(livros_nosDisponiveis, f, ensure_ascii=False, indent=4)

            else:
                print(
                    'Você tem três livros emprestados, devolva um e você poderá pegar outro'
                )

    def livrosEmprestados(self):
        print('Atualmente você pegou os seguintes livros emprestados: ')
        for i, emprestado in enumerate(self.emprestados):
            print(f'indice: -{i} {emprestado}')

    def devolverLivro(self, indice):
        if indice in range(len(self.emprestados)):
            devolvido = self.emprestados.pop(indice)
            self.disponiveis.append(devolvido)
            print('Livro devolvido com sucesso!')
        else:
            print('Índice inválido!')


def main():
    while True:
        print()
        desejaFazer = input(
            'Você deseja [R]egistrar um livro, [V]er os livros, [E]mprestar um livro, [O]lhar quais livros emprestados ou [D]evolver um livro? '
        ).upper()

        if desejaFazer == 'R':
            print()
            try:
                # registarLivro()
                print('livro registrado com sucesso!')
            except ValueError:
                print('Digite o ano de publicação do livro, não um texto')

        elif desejaFazer == 'V':
            print()
            # verLivros()

        elif desejaFazer == 'E':
            print()
            # try:
            # emprestimo = int(
            # input('Digite o indice do livro que você deseja pegar emprestado: ')
            # )
            # emprestar(emprestimo)
            # except ValueError:
            # print('Digite o indice do livro, não um texto')

        elif desejaFazer == 'O':
            print()
            # livrosEmprestados()

        elif desejaFazer == 'D':
            print()
            # try:
            #     indiceDevolver = int(
            #         input('Digite o indice do livro que você deseja devolver: ')
            #     )
            #     devolverLivro(indiceDevolver)
            # except ValueError:
            #     print('Digite o indice do livro, não um texto')

        print()
        pergunta = input('Você deseja continuar? (S/N) ').upper()
        if pergunta != 'S':
            break


if __name__ == '__main__':
    main()
