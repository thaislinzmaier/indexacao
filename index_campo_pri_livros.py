import csv

def index_campo_pri_livros():
    #local e nome do arquivo original
    arquivo = r'G:\Meu Drive\Ciência da Computação\2022 4\Algoritmos e Estrutura de Dados 2\Trabalho\books_data.csv'

    #fixando o tamanho dos campos do cabeçalho
    contador_header = 'Chave'
    contador_header = "{:<20}".format(contador_header)
    titulo_header = 'Título'
    titulo_header = "{:<500}".format(titulo_header)
    autores_header = 'Autores'
    autores_header = "{:<400}".format(autores_header)
    editora_header = 'Editora'
    editora_header = "{:<100}".format(editora_header)
    data_publicacao_header = 'Data de Publicação'
    data_publicacao_header = "{:<100}".format(data_publicacao_header)
    categorias_header = 'Categorias'
    categorias_header = "{:<100}".format(categorias_header)
    avaliacao_header = 'Avaliação'
    avaliacao_header = "{:<20}".format(avaliacao_header)

    #abertura do arquivo original e leitura linha por linha
    with open(arquivo, newline='', encoding='utf-8-sig') as csvfile:
        data = csv.DictReader(csvfile)
        #abertura do arquivo de escrita indexada
        with open('arquivos/arquivo_index_pri_livros.csv', 'w', encoding='utf-8') as arquivo_tam_fixo:
            #montagem do cabeçalho
            cabecalho = contador_header + ','\
                        + titulo_header + ','\
                        + autores_header + ','\
                        + editora_header + ','\
                        + data_publicacao_header + ','\
                        + categorias_header + ','\
                        + avaliacao_header
            #escrita do cabeçalho
            arquivo_tam_fixo.write(cabecalho)
            arquivo_tam_fixo.write('\n')
            #inicialização do contador para a formação do campo chave
            cont = 0
            #leitura das linhas do arquivo original
            for r in data:
                #incrementação do campo chave
                cont = cont + 1
                #transformação do campo chave para string para poder ser inserido com tamanho fixo no arquivo
                contador_str = str(cont)
                contador_str = "{:<20}".format(contador_str)
                #fixando o tamanho dos campos do arquivo
                titulo = r['Title']
                titulo = "{:<500}".format(titulo)
                autores = r['authors']
                autores = "{:<400}".format(autores)
                editora = r['publisher']
                editora = "{:<100}".format(editora)
                data_publicacao = r['publishedDate']
                data_publicacao ="{:<100}".format(data_publicacao)
                categorias = r['categories']
                categorias = "{:<100}".format(categorias)
                num_avaliacoes =  r['ratingsCount']
                num_avaliacoes = "{:<20}".format(num_avaliacoes)
                #concatenação dos valores de cada linha
                linha = contador_str + ',' \
                    + titulo + ',' \
                    + autores + ',' \
                    + editora + ',' \
                    + data_publicacao + ','\
                    + categorias + ',' \
                    + num_avaliacoes
                #escrita da linha no novo arquivo
                arquivo_tam_fixo.write(linha)
                arquivo_tam_fixo.write('\n')


                