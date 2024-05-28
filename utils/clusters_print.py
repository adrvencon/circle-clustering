def print_clusters(result_clusters, assigned_points):
    for i, cluster in enumerate(result_clusters):
        print(f"CLUSTER {i+1}:")
        print(f"Estimated Center = {cluster.center}, Estimated Radius = {cluster.radius}") 
        print("------------------------------------------------------------------")
        print(f"Assigned points = {assigned_points}")
        print("")