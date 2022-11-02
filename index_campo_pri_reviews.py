import csv

def index_campo_pri_reviews():
    #local e nome do arquivo original
    arquivo = r'G:\Meu Drive\Ciência da Computação\2022 4\Algoritmos e Estrutura de Dados 2\Trabalho\Books_rating.csv'

    #fixando o tamanho dos campos do cabeçalho
    contador_header = 'Chave'
    contador_header = "{:<20}".format(contador_header)
    id_header ='Id'
    id_header = "{:<20}".format(id_header)
    titulo_header = 'Título'
    titulo_header = "{:<200}".format(titulo_header)
    avaliacao_header = 'Avaliação'
    avaliacao_header = "{:<20}".format(avaliacao_header)
   
    #abertura do arquivo original e leitura linha por linha
    with open(arquivo, newline='', encoding='utf-8-sig') as csvfile:
        data = csv.DictReader(csvfile)
        #abertura do arquivo de escrita indexada
        with open('arquivos/arquivo_index_pri_reviews.csv', 'w', encoding='utf-8') as arquivo_tam_fixo:
            #montagem do cabeçalho
            cabecalho = contador_header + ',' \
            + id_header + ','\
            + titulo_header + ','\
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
                Id = r['Id']
                Id = "{:<20}".format(Id)
                titulo = r['Title']
                titulo = "{:<200}".format(titulo)
                avaliacao =  r['review/score']
                avaliacao = "{:<20}".format(avaliacao)
                #concatenação dos valores de cada linha
                linha = contador_str + ','\
                    + Id + ','\
                    + titulo +','\
                    + avaliacao
                #escrita da linha no novo arquivo
                arquivo_tam_fixo.write(linha)
                arquivo_tam_fixo.write('\n')


                