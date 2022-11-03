from index_campo_pri_livros import *
from index_campo_pri_reviews import *
from index_campo_sec_livros import *
from pesquisa_arquivos import *
from pesquisa_memoria import *
from arvore import *

if __name__ == '__main__':

    print("Selecione a ação:")
    print("1 - Gerar chave primária no arquivo de livros e reviews")
    print("2 - Gerar chave secundária no arquivo de livros")
    print("3 - Pesquisar nos arquivos")
    print("4 - Gerar chaves em memória para livros e reviews e pesquisar")
    print("5 - Gerar árvore de pesquisa para livros e reviews e pesquisar")

    opcao = input()

    if opcao == '1':
        index_campo_pri_livros()
        index_campo_pri_reviews()
    if opcao == '2':
        index_campo_sec_livros()
    if opcao == '3':
        print("Escolha o que quer pesquisar:")
        print("1 - TOP 10 livros mais bem avaliados")
        print("2 - TOP 10 livros mais mal avaliados")
        opcao_int = input()
        if opcao_int == '1':
            print("Localizando os 10 livros mais bem avaliados, por favor aguarde!")
            top10()
        if opcao_int == '2':
            print("Localizando os 10 livros mais mal avaliados, por favor aguarde!")
            top10_piores()
    if opcao == '4':
        print("Escolha o que quer pesquisar:")
        print("1 - TOP 10 livros mais bem avaliados")
        print("2 - TOP 10 livros mais mal avaliados")
        opcao_int = input()
        if opcao_int == '1':
            print("Localizando os 10 livros mais bem avaliados, por favor aguarde!")
            top10_mem()
        if opcao_int == '2':
            print("Localizando os 10 livros mais mal avaliados, por favor aguarde!")
            top10_piores_mem()
    if opcao == '5':
        print("TOP 10 autores com mais avaliações")
        cria_arquivo()
