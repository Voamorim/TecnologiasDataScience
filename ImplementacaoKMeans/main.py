from kmeans import KMeans

dados1 = "./Data/dados_1_simples.csv"
dados2 = "./Data/dados_2_3clusters.csv"
dados3 = "./Data/dados_3_3d.csv"
dados4 = "./Data/dados_5_4d_120entradas.csv"

def solve(it, k, dados, idx):
    kmeans = KMeans()

    print("=-" * 30)
    print(" " * 25, end="")
    print(f"Dados {idx}")
    print("=-" * 30)

    clusters, centroids = kmeans.run_k_means(dados, it, k)

    for i, c in enumerate(clusters):
        print(f'cluster {i}:')
        
        for p in c.points:
            p.print()
        print()
        print(f'centroid: {centroids[i].coordinates}')
        print()

k = 2
it = 50
solve(it, k, dados1, 1)

k = 3
it = 50
solve(it, k, dados2, 2)

k = 2
it = 50
solve(it, k, dados3, 3)


k = 3
it = 50
solve(it, k, dados4, 4)
