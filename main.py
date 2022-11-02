from index_campo_pri_livros import *
from index_campo_pri_reviews import *
from index_campo_sec_livros import *


#---------------------------#
#pesquisa_sequencial_indexado()
#index_campo_sec_reviews()
#pesquisa_index_campo_sec()
#index_campo_terc_livros()
#index_campo_terc_reviews()
#pesquisa_index_campo_terc()
#index_campo_qua_livros()
#index_campo_qua_reviews()
#pesquisa_index_campo_qua()


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
        pesquisa_arquivos()
