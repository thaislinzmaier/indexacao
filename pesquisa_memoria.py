#10 livros com mais avaliações
#Editoras mais avaliadas
#Autores mais avaliados


import csv, sys

def has_numbers(inputString):
        return any(char.isdigit() for char in inputString)

def top10_mem():
    maxInt = sys.maxsize
    while True:
        try:
            csv.field_size_limit(maxInt)
            break
        except OverflowError:
            maxInt = int(maxInt/10)

    arquivo = r'G:\Meu Drive\Ciência da Computação\2022 4\Algoritmos e Estrutura de Dados 2\Trabalho\arquivos\arquivo_index_pri_livros.csv'

    with open(arquivo, encoding='utf-8') as arq:
        data = csv.DictReader(arq, delimiter=',')
        lista_avaliacao = []
        for i in data:
            pesq_chave = 'Chave'
            chave = "{:<20}".format(pesq_chave)
            pesq_aval = 'Avaliação'
            avaliacoes = "{:<20}".format(pesq_aval)
            if has_numbers(str(i[avaliacoes])):
                if '.' in i[avaliacoes]:
                    chave_aval = i[chave] + ',' + i[avaliacoes]
                    lista_avaliacao.append(chave_aval)
    top10 = []
    for i in lista_avaliacao:
        aval = i.split(',')[1]
        chave = i.split(',')[0]
        linha = aval + ',' + chave
        top10.append(linha)
    resultado = sorted(top10)
    resultado_t10 = resultado[:10]

    titulos = []
    for i in resultado_t10:
        chave = i.split(',')[1]
        with open(arquivo, encoding='utf-8') as arq:
            data = csv.DictReader(arq, delimiter=',')
            for j in data:
                pesq_titulo = 'Título'
                titulo = "{:<500}".format(pesq_titulo)
                pesq_chave = 'Chave'
                chave_arq = "{:<20}".format(pesq_chave)
                if chave == j[chave_arq]:
                    titulos.append(j[titulo])
    for i in titulos:
        i.strip()
        print(i)
            

def top10_piores_mem():    
    maxInt = sys.maxsize
    while True:
        try:
            csv.field_size_limit(maxInt)
            break
        except OverflowError:
            maxInt = int(maxInt/10)

    arquivo = r'G:\Meu Drive\Ciência da Computação\2022 4\Algoritmos e Estrutura de Dados 2\Trabalho\arquivos\arquivo_index_pri_livros.csv'

    with open(arquivo, encoding='utf-8') as arq:
        data = csv.DictReader(arq, delimiter=',')
        lista_avaliacao = []
        for i in data:
            pesq_chave = 'Chave'
            chave = "{:<20}".format(pesq_chave)
            pesq_aval = 'Avaliação'
            avaliacoes = "{:<20}".format(pesq_aval)
            if has_numbers(str(i[avaliacoes])):
                if '.' in i[avaliacoes]:
                    chave_aval = i[chave] + ',' + i[avaliacoes]
                    lista_avaliacao.append(chave_aval)
    top10 = []
    for i in lista_avaliacao:
        aval = i.split(',')[1]
        chave = i.split(',')[0]
        linha = aval + ',' + chave
        top10.append(linha)
    resultado = sorted(top10, reverse=True)
    resultado_t10 = resultado[:10]

    titulos = []
    for i in resultado_t10:
        chave = i.split(',')[1]
        with open(arquivo, encoding='utf-8') as arq:
            data = csv.DictReader(arq, delimiter=',')
            for j in data:
                pesq_titulo = 'Título'
                titulo = "{:<500}".format(pesq_titulo)
                pesq_chave = 'Chave'
                chave_arq = "{:<20}".format(pesq_chave)
                if chave == j[chave_arq]:
                    titulos.append(j[titulo])
    for i in titulos:
        i.strip()
        print(i)
    
    