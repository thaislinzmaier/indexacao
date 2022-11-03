#10 livros com mais avaliações
#Editoras mais avaliadas
#Autores mais avaliados


import csv, sys
import operator

def has_numbers(inputString):
        return any(char.isdigit() for char in inputString)

def top10():
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
            

def top10_piores():    
    maxInt = sys.maxsize
    while True:
        try:
            csv.field_size_limit(maxInt)
            break
        except OverflowError:
            maxInt = int(maxInt/10)

    arquivo = r'G:\Meu Drive\Ciência da Computação\2022 4\Algoritmos e Estrutura de Dados 2\Trabalho\arquivos\arquivo_index_pri_livros.csv'
    arquivo_top_10_piores = r'G:\Meu Drive\Ciência da Computação\2022 4\Algoritmos e Estrutura de Dados 2\Trabalho\arquivos\top_10_piores.csv'
    arquivo_top_10_piores_ordenado = r'G:\Meu Drive\Ciência da Computação\2022 4\Algoritmos e Estrutura de Dados 2\Trabalho\arquivos\top_10_piores_ordenado.csv'
    arquivo_lista_piores_livros = r'G:\Meu Drive\Ciência da Computação\2022 4\Algoritmos e Estrutura de Dados 2\Trabalho\arquivos\top_10_piores_livros.csv'
    arquivo_livros_mal_avaliados = r'G:\Meu Drive\Ciência da Computação\2022 4\Algoritmos e Estrutura de Dados 2\Trabalho\arquivos\top_10_piores_livros_titulos.csv'



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
    
    with open(arquivo_top_10_piores, 'w', encoding='utf-8') as arq_top_10_p:
        pesq_chave = 'Chave'
        chave = "{:<20}".format(pesq_chave)
        pesq_aval = 'Avaliação'
        avaliacoes = "{:<20}".format(pesq_aval)
        cabecalho = avaliacoes + ',' + chave
        arq_top_10_p.write(cabecalho)
        arq_top_10_p.write('\n')
        for i in lista_avaliacao:
            aval = i.split(',')[1]
            chave = i.split(',')[0]
            linha = aval + ',' + chave
            arq_top_10_p.write(linha)
            arq_top_10_p.write('\n')

    with open(arquivo_top_10_piores, 'r', encoding='utf-8') as arq_top_10_p:
        with open(arquivo_top_10_piores_ordenado, 'w', encoding='utf-8') as arq_top_10_p_o:
            pesq_chave = 'Chave'
            chave = "{:<20}".format(pesq_chave)
            pesq_aval = 'Avaliação'
            avaliacoes = "{:<20}".format(pesq_aval)
            cabecalho = avaliacoes + ',' + chave
            arq_top_10_p_o.write(cabecalho)
            arq_top_10_p_o.write('\n')
            data = csv.DictReader(arq_top_10_p, delimiter=",")
            lista_avaliacao_ordenada = []
            for i in data:
                avaliacao = i[avaliacoes]
                chaves = i[chave]
                if not any(c.isalpha() for c in avaliacao):
                    linha = avaliacao + ',' + chaves
                    lista_avaliacao_ordenada.append(linha)
            lista_avaliacao_ordenada.sort()
            resultado = lista_avaliacao_ordenada[:10]
            for i in resultado:
                arq_top_10_p_o.write(i)
                arq_top_10_p_o.write('\n')
    
    with open(arquivo, 'r', encoding='utf-8') as arq_top_10_p_o:
        with open(arquivo_top_10_piores_ordenado, 'r', encoding='utf-8') as arq:
            data1 = csv.DictReader(arq_top_10_p_o)
            pesq_titulo = 'Título'
            titulo = "{:<500}".format(pesq_titulo)
            pesq_chave = 'Chave'
            chave = "{:<20}".format(pesq_chave)
            data2 = csv.DictReader(arq)
            with open(arquivo_livros_mal_avaliados, 'w', encoding='utf-8') as alma:             
                lista_chaves = []
                for i in data2:
                    lista_chaves.append(i[chave])
                for j in data1:
                    for i in lista_chaves:
                        if i == j[chave]:
                            alma.write(j[titulo])
                            alma.write('\n')
                        
                        
    
 
    
    