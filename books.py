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
        for disponiveis in self.disponiveis:
            print(disponiveis)

    def emprestar(self, nome):
        for livro in self.disponiveis:
            if livro.nome.lower() == nome.lower():
                if len(self.emprestados) < 3:
                    self.disponiveis.remove(livro)
                    self.emprestados.append(livro)
                    print('Livro emprestado com sucesso!')
                else:
                    print('Você já pegou 3 livros, se quiser pegar mais um devolva um!')
            return
        print('Livro não encontrado!')

    def livrosEmprestados(self):
        print('Atualmente você pegou os seguintes livros emprestados: ')
        for emprestados in self.emprestados:
            print(emprestados)

    def devolverLivro(self, nome):
        for livro in self.emprestados:
            if livro.nome.lower() == nome.lower():
                self.emprestados.remove(livro)
                self.disponiveis.append(livro)
                print('Livro removido com sucesso!!')
                self._salvar_json()
            return
        print('Livro não encontrado!')

    def removerLivro(self, nome):
        for livro in self.disponiveis:
            if livro.nome.lower() == nome.lower():
                self.disponiveis.remove(livro)
                print('Livro removido com sucesso!!')
                self._salvar_json()
            return

    print('Livro não encontrado!')


def main():
    biblioteca = Biblioteca()

    while True:
        oque_fazer = input(
            'Você deseja [A]dicionar um livro? [V]er os livros disponiveis? [E]mprestar um livro? [Q]auis livros você pegou emprestado? [D]evolver um livro? [R]emover um livro?  '
        ).upper()

        match oque_fazer:
            case 'A':
                try:
                    nome = str(input('Digite o nome do livro: '))
                    genero = str(input('Digite o genero do livro: '))
                    autor = str(input('Digite o nome do autor: '))
                    anoPublicado = int(input('Digite o ano de publicação do livro: '))
                    biblioteca.registarLivro(nome, genero, autor, anoPublicado)
                except ValueError:
                    print(
                        'Digite o ano de publicação ou um texto nos campos de nome, genero e autor '
                    )

            case 'V':
                biblioteca.verLivros()

            case 'E':
                try:
                    indice = int(input('Digite o indice do livro: '))
                    biblioteca.emprestar(indice)
                except ValueError:
                    print('Digite um numero (indice), não um texto!!')

            case 'Q':
                biblioteca.livrosEmprestados()

            case 'D':
                try:
                    indice2 = int(
                        input('Digite o indice do livro que deseja devolver: ')
                    )
                    biblioteca.devolverLivro(indice2)
                except ValueError:
                    print('Por favor, digite um número (indice), não um texto!!!')

            case 'R':
                try:
                    indice3 = int(
                        input('Digite o indice do livro que você deseja remover: ')
                    )
                    biblioteca.removerLivro(indice3)
                except ValueError:
                    print('Digite um número (indice), não um texto!!!')
        print()
        pergunta = input('Você deseja continuar? (S/N) ').upper()
        if pergunta != 'S':
            break


if __name__ == '__main__':
    main()
