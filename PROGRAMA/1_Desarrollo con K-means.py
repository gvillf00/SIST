# -*- coding: utf-8 -*-


import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# variables que ponemos por defecto para qeu no salgan advertencias
# super()._check_params_vs_input(default_n_init=10)

OMP_NUM_THREADS=1

######## df = pd.read_csv('D:/GEMMA/UNIVERSIDAD/PruebaSIST.csv')


data = {'barrio': ['A', 'B', 'C', 'D'],'ninos': [100, 150, 50, 200],'lat': [37.7749, 37.7750, 37.7751, 37.7752],'lon': [-122.4194, -122.4195, -122.4196, -122.4197]}
df = pd.DataFrame(data)



# Usando K-Means para encontrar el centro de los clusters de barrios con más niños
######## kmeans = KMeans(n_clusters=1, random_state=0).fit(df[['NOMBRE_BARRIO']], sample_weight=df['< 12'])
kmeans = KMeans(n_clusters=1, random_state=0).fit(df[['lat', 'lon']], sample_weight=df['ninos'])


# Graficando los resultados
########plt.scatter(df['NOMBRE_BARRIO'], s=df['< 12'])
plt.scatter(df['lat'], df['lon'], s=df['ninos'])
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red')
plt.show()
