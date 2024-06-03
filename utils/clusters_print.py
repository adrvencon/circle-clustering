import numpy as np

def print_clusters(result_clusters, assigned_points, centers=[], radii=[]):
    parsed_centers = [centers[i:i+2] for i in range(0, len(centers), 2)]
    for i, cluster in enumerate(result_clusters):
        if len(parsed_centers) != 0:
            closest_center = min(parsed_centers, key=lambda x: np.linalg.norm(np.array(x) - np.array(cluster.center)))
            center_error = np.linalg.norm(closest_center - cluster.center)
            closest_radius = radii[np.abs(radii - cluster.radius).argmin()]
            radius_error = np.abs(closest_radius - cluster.radius)
            accumulated_error = center_error + radius_error
            print(f"CLUSTER {i+1}:")
            print(f"Estimated Center = {cluster.center}, Estimated Radius = {cluster.radius}") 
            print("------------------------------------------------------------------")
            print(f"Center Error = {center_error}, Radius Error = {radius_error}, Accumulated Error = {accumulated_error}")
            print("------------------------------------------------------------------")
            print(f"Assigned points = {assigned_points}")
            print("")
            total_error =+ accumulated_error
        else:
            print(f"CLUSTER {i+1}:")
            print(f"Estimated Center = {cluster.center}, Estimated Radius = {cluster.radius}") 
            print("------------------------------------------------------------------")
            print(f"Assigned points = {assigned_points}")
            print("")
    if len(parsed_centers) >= 2:
        print(f"Total Error (All Clusters) = {total_error}")
        print("")


