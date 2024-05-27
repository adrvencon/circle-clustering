import matplotlib.pyplot as plt
from matplotlib.patches import Circle

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def plot_clusters(points, result_clusters):
    plt.figure(figsize=(10, 10))
    plt.scatter(points[:, 0], points[:, 1], c='b', label='Data')

    for i, cluster in enumerate(result_clusters):
        circle = Circle(cluster.center, cluster.radius, color='r', fill=False, linestyle='--', linewidth=2)
        plt.gca().add_patch(circle)
        plt.scatter(cluster.center[0], cluster.center[1], c='r', marker='x', label='Cluster Center')

    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.title('Ring Clustering Experiment')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()