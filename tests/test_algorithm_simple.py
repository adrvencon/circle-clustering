import numpy as np
import matplotlib.pyplot as plt

from clustering.algorithm.algorithm import ring_clustering
from utils.circle_generator import generate_circle_points
from utils.plot_clusters import plot_clusters
from utils.print_clusters import print_clusters

circle_params = [
    {"center": (0, 0), "radius": 2, "num_points": 30},
    {"center": (1, 1), "radius": 4, "num_points": 30}
]

points = np.concatenate([generate_circle_points(**params) for params in circle_params])

num_clusters = 2
result_clusters, assigned_points = ring_clustering(points, num_clusters)

print_clusters(result_clusters, assigned_points)
plot_clusters(points, result_clusters)