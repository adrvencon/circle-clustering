def print_clusters(result_clusters, assigned_points):
    for i, cluster in enumerate(result_clusters):
        print(f"Cluster {i+1}: Center={cluster.center}, Radius={cluster.radius}, Assigned points={assigned_points}")