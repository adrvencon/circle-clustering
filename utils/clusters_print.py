import numpy as np

def print_clusters(result_clusters, assigned_points, centers=[], radii=[]):
    for i, cluster in enumerate(result_clusters):

        if len(centers) != 0:
            center_error = np.linalg.norm(centers[i] - cluster.center)
            radius_error = np.abs(radii[i] - cluster.radius)
            accumulated_error = center_error + radius_error
            print(f"CLUSTER {i+1}:")
            print(f"Estimated Center = {cluster.center}, Estimated Radius = {cluster.radius}") 
            print("------------------------------------------------------------------")
            print(f"Center Error = {center_error}, Radius Error = {radius_error}, Accumulated Error = {accumulated_error}")
            print("------------------------------------------------------------------")
            print(f"Assigned points = {assigned_points}")
            print("")
        else:
            print(f"CLUSTER {i+1}:")
            print(f"Estimated Center = {cluster.center}, Estimated Radius = {cluster.radius}") 
            print("------------------------------------------------------------------")
            print(f"Assigned points = {assigned_points}")
            print("")


