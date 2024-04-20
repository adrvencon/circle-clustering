import numpy as np
import matplotlib.pyplot as plt
from clustering.algorithm.algorithm import ring_clustering
from utils.circle_generator import generate_circle_points
from utils.plot_clusters import plot_clusters
from utils.print_clusters import print_clusters

circle_params = [
    {"center": (1, 2), "radius": 3, "num_points": 40},
    {"center": (20, 20), "radius": 4, "num_points": 80},
    {"center": (60, 80), "radius": 6, "num_points": 60}
]

points = np.concatenate([generate_circle_points(**params) for params in circle_params])

# Add some noise to the points.
noise = np.random.normal(0, 1, size=points.shape)
noisy_points = points + noise

num_clusters = 3
result_clusters = ring_clustering(noisy_points, num_clusters)

print_clusters(result_clusters)
plot_clusters(points, result_clusters)