from point import Point 
from cluster import Cluster

import random
import csv
import copy

INF = 1_000_000_000

class KMeans:
    def __init__(self):
        pass

    def read_csv(self, input_file: str):
        dict_csv = list()

        with open(input_file, mode='r') as file:
            reader = csv.reader(file)

            # pula o header do csv
            next(reader)

            for row in reader:
                dict_csv.append(row)

        return dict_csv

    def get_points(self, dados):
        points = []
        for coordinates in dados:
            points.append(Point(list(map(float, coordinates))))
        
        return points

    def get_random_points(self, points, k):
        return random.sample(points, k)

    def run_k_means(self, input_file:str, n:int, k:int):
        dados = self.read_csv(input_file)
        points = self.get_points(dados)

        centroides = self.get_random_points(points, k)
        
        clusters = []
        for i in range(n):
            clusters = [Cluster() for _ in range(k)]
            
            for p in points:
                min_dist = -INF
                cluster_idx = -1 

                for c in range(k):
                    dist = p.euclidean_distance(centroides[c])
                    
                    if dist < min_dist:
                        min_dist = dist
                        cluster_idx = c
         
                clusters[cluster_idx].add_point(p)

            novos_centroides = []
            for i in range(k):
                # Caso nao esteja vazio
                if(len(clusters[i].points) > 0):
                    clusters[i].new_centroid() 
                    novos_centroides.append(clusters[i].centroid) 
                else: 
                    novos_centroides.append(centroides[i])

            # Critério de parada: centroides nao mudaram
            if novos_centroides == centroides:
                break
            
            centroides = novos_centroides

        return clusters, centroides
