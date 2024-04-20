import numpy as np
import matplotlib.pyplot as plt

from clustering.algorithm.algorithm import ring_clustering
from utils.plot_clusters import plot_clusters
from utils.print_clusters import print_clusters

np.random.seed(0)
num_points = 100
points = np.random.uniform(low=0, high=100, size=(num_points, 2))

num_clusters = 3
result_clusters, assigned_points = ring_clustering(points, num_clusters)

print_clusters(result_clusters, assigned_points)
plot_clusters(points, result_clusters)