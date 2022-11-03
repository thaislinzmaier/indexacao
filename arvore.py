import csv

arquivo = r'G:\Meu Drive\Ciência da Computação\2022 4\Algoritmos e Estrutura de Dados 2\Trabalho\arquivos\arquivo_index_pri_livros.csv'
arquivo_autores = r'G:\Meu Drive\Ciência da Computação\2022 4\Algoritmos e Estrutura de Dados 2\Trabalho\arquivos\arquivo_autores_arvore.csv'



def cria_arquivo():
    with open(arquivo, 'r', encoding='utf-8') as arq:
        data = csv.DictReader(arq)
        autores_header = 'Autores'
        autores_header = "{:<400}".format(autores_header)
        contador_header = 'Chave'
        contador_header = "{:<20}".format(contador_header)
        with open(arquivo_autores, 'w', encoding='utf-8') as arq_aut:
            cabecalho = contador_header + ',' + autores_header
            arq_aut.write(cabecalho)
            arq_aut.write('\n')
            autores = []
            cont = 0
            for i in data:
                if i[autores_header] not in autores:
                    cont += 1
                    contador = str(cont)
                    contador = "{:<20}".format(contador)
                    autores.append(i[autores_header])
                    linha = contador + ',' + i[autores_header]
                    arq_aut.write(linha)
                    arq_aut.write('\n')

def pesquisa_arvore():
    B = BTree(3)
    with open(arquivo_autores, 'r', encoding='utf-8') as autores:
        data = csv.DictReader(autores)
        autores_header = 'Autores'
        autores_header = "{:<400}".format(autores_header)
        contador_header = 'Chave'
        contador_header = "{:<20}".format(contador_header)
        for i in data:
            B.insert((int(i[contador_header]), 2 * int(i[contador_header])))



class BTreeNode:
  def __init__(self, leaf=False):
    self.leaf = leaf
    self.keys = []
    self.child = []


# Tree
class BTree:
  def __init__(self, t):
    self.root = BTreeNode(True)
    self.t = t

    # Insert node
  def insert(self, k):
    root = self.root
    if len(root.keys) == (2 * self.t) - 1:
      temp = BTreeNode()
      self.root = temp
      temp.child.insert(0, root)
      self.split_child(temp, 0)
      self.insert_non_full(temp, k)
    else:
      self.insert_non_full(root, k)

    # Insert nonfull
  def insert_non_full(self, x, k):
    i = len(x.keys) - 1
    if x.leaf:
      x.keys.append((None, None))
      while i >= 0 and k[0] < x.keys[i][0]:
        x.keys[i + 1] = x.keys[i]
        i -= 1
      x.keys[i + 1] = k
    else:
      while i >= 0 and k[0] < x.keys[i][0]:
        i -= 1
      i += 1
      if len(x.child[i].keys) == (2 * self.t) - 1:
        self.split_child(x, i)
        if k[0] > x.keys[i][0]:
          i += 1
      self.insert_non_full(x.child[i], k)

    # Split the child
  def split_child(self, x, i):
    t = self.t
    y = x.child[i]
    z = BTreeNode(y.leaf)
    x.child.insert(i + 1, z)
    x.keys.insert(i, y.keys[t - 1])
    z.keys = y.keys[t: (2 * t) - 1]
    y.keys = y.keys[0: t - 1]
    if not y.leaf:
      z.child = y.child[t: 2 * t]
      y.child = y.child[0: t - 1]

  # Print the tree
  def print_tree(self, x, l=0):
    print("Level ", l, " ", len(x.keys), end=":")
    for i in x.keys:
      print(i, end=" ")
    print()
    l += 1
    if len(x.child) > 0:
      for i in x.child:
        self.print_tree(i, l)

  # Search key in the tree
  def search_key(self, k, x=None):
    if x is not None:
      i = 0
      while i < len(x.keys) and k > x.keys[i][0]:
        i += 1
      if i < len(x.keys) and k == x.keys[i][0]:
        return (x, i)
      elif x.leaf:
        return None
      else:
        return self.search_key(k, x.child[i])
      
    else:
      return self.search_key(k, self.root)


def main():
    B = BTree(3)

    pesquisa_arvore()
            

    B.print_tree(B.root)

    if B.search_key(8) is not None:
        print("\nFound")
    else:
        print("\nNot Found")


if __name__ == '__main__':
  main()


