import csv
import random

import networkx as nx
import numpy as np

class LabelPropagation:
    def __init__(self):
        self.graph = nx.Graph()
        self.labels = list()  
        self.n = 0 
        self.m = 0

    def read_graph(self, input_file:str):
        dict_csv = list()

        with open(input_file, mode='r') as file:
            reader = csv.reader(file)

            # pula o header do csv
            next(reader)

            for row in reader:
                dict_csv.append(row)
       
        for _, edge in enumerate(dict_csv):
            e = (list(map(int, edge)))
            self.graph.add_edge(e[0], e[1])
    
        self.m = self.graph.number_of_edges()
        self.n = self.graph.number_of_nodes()

        # Atribui o indice do no como o label original
        self.labels = [x for x in range(len(self.labels))]

    def propagate_labels(self, node:int):
        if self.graph.degree(node) == 0:
            return

        neighbors_array = list(self.graph.neighbors(node))
        label_freq = [0 for _ in range(self.n + 1)]
        
        for u in neighbors_array:
            label_freq[self.labels[u]] += 1 

        highest_freq = max(label_freq)
        most_freq = [i for i, freq in enumerate(label_freq) if freq == highest_freq]
        
        self.labels[node] = random.choice(most_freq)

    def run(self, max_iterations:int):
        changed = True 

        for _ in range(max_iterations):
            if not changed: break
            changed = False
          
            # Inicializa a lista da ordem de acesso aleatória dos nós
            rng = np.random.default_rng()
            node_order = np.arange(1, self.n + 1)
            rng.shuffle(node_order)

            for v in np.nditer(node_order):

            
