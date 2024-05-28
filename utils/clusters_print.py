import numpy as np

def print_clusters(result_clusters, assigned_points, centers, radii):
    for i, cluster in enumerate(result_clusters):
        center_error = np.linalg.norm(centers[i] - cluster.center)
        radius_error = np.abs(radii[i] - cluster.radius)
        print(f"CLUSTER {i+1}:")
        print(f"Estimated Center = {cluster.center}, Estimated Radius = {cluster.radius}") 
        print("------------------------------------------------------------------")
        print(f"Center Error = {center_error}, Radius Error = {radius_error}")
        print("------------------------------------------------------------------")
        print(f"Assigned points = {assigned_points}")
        print("")