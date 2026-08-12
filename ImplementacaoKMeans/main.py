from typing import ForwardRef

from kmeans import KMeans

dados1 = "./Data/dados_1_simples.csv"
dados2 = "./Data/dados_2_3clusters.csv"
dados3 = "./Data/dados_3_3d.csv"
dados4 = "./Data/dados_5_4d_120entradas.csv"

kmeans = KMeans()

k = 2
it = 50
clusters, centroids = kmeans.run_k_means(dados1, it, k)

for i, c in enumerate(clusters):
    print(f'cluster {i}:')
    
    for p in c.points:
        p.print()

"""
k = 3
it = 50
clusters, centroids = kmeans.run_k_means(dados2, it, k)
print(f'clusters: ', clusters)
print(f'centroids: ', centroids)

k = 2
it = 50
clusters, centroids = kmeans.run_k_means(dados3, it, k)
print(f'clusters: ', clusters)
print(f'centroids: ', centroids)

k = 3
it = 50
clusters, centroids = kmeans.run_k_means(dados4, it, k)
print(f'clusters: ', clusters)
print(f'centroids: ', centroids)
"""
