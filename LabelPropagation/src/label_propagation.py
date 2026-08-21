import csv
import random

import networkx as nx
import numpy as np

class LabelPropagation:
    def __init__(self):
        self.graph = nx.Graph()
        self.labels = dict()  
        self.n = 0 # Numero de vertices
        self.m = 0 # Numero de arestas

    def read_graph(self, input_file:str):
        """
        Lê o grafo do arquivo .csv e atribui o próprio identificador como 
        label inicial.
        """
        dict_csv = list()

        with open(input_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader) # pula o header do csv
            for row in reader:
                dict_csv.append(row)
       
        for _, edge in enumerate(dict_csv):
            e = (list(map(int, edge)))
            self.graph.add_edge(e[0], e[1]) # aresta não direcionada
    
        self.m = self.graph.number_of_edges()
        self.n = self.graph.number_of_nodes()

        # Atribui o indice do no como o label original
        for v in list(self.graph.nodes):
            self.labels[v] = v

    def propagate_labels(self, node:int):
        """
        Propaga o label mais frequente dos vizinhos do nó `node` para ele. Em 
        caso de empate, é selecionado aleatoriamente um dos labels mais 
        frequentes.

        Retorna um booleano identificando se o label foi modificado ou não.
        """
        neighbors_array = list(self.graph.neighbors(node))
        label_freq = dict()

        # computa a frequência dos labels dos nós vizinhos
        for u in neighbors_array:
            if self.labels[u] in label_freq.keys():
                label_freq[self.labels[u]] += 1 
            else:
                label_freq[self.labels[u]] = 1

        # extrai a maior frequência obtida
        highest_freq = max(label_freq.values())
       
        # seleciona aleatoriamente um dos labels com maior frequência
        most_freq = list() 
        for key, value in label_freq.items():
            if value == highest_freq:
                most_freq.append(key)
        chosen = random.choice(most_freq)

        if self.labels[node] == chosen:
            return False

        self.labels[node] = chosen 
        return True

    def run(self, max_iterations:int, input_file:str):
        self.read_graph(input_file)

        changed = True 

        for _ in range(max_iterations):
            if not changed: break
            changed = False
          
            # Inicializa a lista da ordem de acesso aleatória dos nós
            rng = np.random.default_rng()
            node_order = np.array(self.graph.nodes())
            rng.shuffle(node_order)

            for v in np.nditer(node_order):
                changed = changed or self.propagate_labels(int(v))
        return list(self.labels.values())
