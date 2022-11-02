import csv, sys

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def index_campo_pri_sec_livros():
    #local e nome do arquivo original
    arquivo = r'G:\Meu Drive\Ciência da Computação\2022 4\Algoritmos e Estrutura de Dados 2\Trabalho\arquivos\arquivo_index_pri_livros.csv'
    arquivo_categorias = r'G:\Meu Drive\Ciência da Computação\2022 4\Algoritmos e Estrutura de Dados 2\Trabalho\arquivos\arquivo_categorias.csv'

    #fixando o tamanho dos campos do cabeçalho
    contador_sec_header = 'Chave Secundária'
    contador_sec_header = "{:<20}".format(contador_sec_header)
    contador_header = 'Chave'
    contador_header = "{:<20}".format(contador_header)
    categorias_header = 'Categorias'
    categorias_header = "{:<100}".format(categorias_header)
    #abertura do arquivo original e leitura linha por linha
    lista_categorias = []
    with open(arquivo, 'r', encoding='utf-8') as csvfile:
        with open(arquivo_categorias, 'w', encoding='utf-8') as arq_cat:
            cabecalho = contador_sec_header + ','\
                        + contador_header + ','\
                        + categorias_header + ','\
            #escrita do cabeçalho
            arq_cat.write(cabecalho)
            arq_cat.write('\n')
            data = csv.reader(csvfile, delimiter = ",")
            contador_sec = 0
            campo_vazio = ' '
            campo_vazio_str = "{:<100}".format(campo_vazio)
            for i in data:
                if i[5] not in lista_categorias:
                    if 'Chave' not in i[5] and 'Categorias' not in i[5]:
                        if not has_numbers(i[5]) and campo_vazio_str not in i[5]:
                            lista_categorias.append(i[5])
                            contador_sec += 1
                            contador_sec_str = str(contador_sec)
                            contador_sec_str = "{:<20}".format(contador_sec_str)
                            linha = contador_sec_str + ',' + i[0] + ',' + i[5]
                            arq_cat.write(linha)
                            arq_cat.write('\n')
                        else:
                            lista_categorias.append(i[5])
                            chave_zero = '0'
                            chave_zero_str = "{:<20}".format(chave_zero)
                            linha = chave_zero_str + ',' + i[0] + ',' + i[5]
                            arq_cat.write(linha)
                            arq_cat.write('\n')
