import numpy as np
import matplotlib.pyplot as plt
from clustering.algorithm.algorithm import ring_clustering
from utils.circle_generator import generate_circle_points, generate_noisy_points
from utils.clusters_plot import plot_clusters
from utils.clusters_print import print_clusters

circle_params = [
    {"center": (1, 2), "radius": 3, "num_points": 80},
    {"center": (3, 5), "radius": 1, "num_points": 80},
    {"center": (10, 10), "radius": 2, "num_points": 80}
]

points = np.concatenate([generate_circle_points(**params) for params in circle_params])

# Add some noise to the points.
noisy_points = generate_noisy_points(points, 0.2)

num_clusters = 3
result_clusters, assigned_points, iterations = ring_clustering(noisy_points, num_clusters)

print_clusters(result_clusters, assigned_points)
plot_clusters(noisy_points, result_clusters)