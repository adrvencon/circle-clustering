import math
import numpy as np

def fit_circle_weighted(points, clusters):
    assigned_points = []
    centers = []
    radii = []
    
    # Separate points into lists based on cluster membership.
    cluster_points = [[] for _ in range(len(clusters))]
    for i, point in enumerate(points):
        max_membership_index = max(range(len(clusters)), key=lambda j: clusters[j].membership_degrees[i])
        cluster_points[max_membership_index].append(point)

    # Check if membership degrees are approximately equal for each point.
    equal_degrees = []
    for i in range(len(points)):
        degrees = [cluster.membership_degrees[i] for cluster in clusters]
        if all(abs(degrees[0] - d) < 0.05 for d in degrees[1:]):
            equal_degrees.append(i)
    
    # If membership degrees are approximately equal for any point, add it to all clusters.
    if equal_degrees:
        for index in equal_degrees:
            for cluster in cluster_points:
                if any(np.all(points[index] == arr) for arr in cluster):
                    cluster_points.append(points[index])

    for i, cluster in enumerate(clusters):
        center = calculate_barycenter(cluster_points[i])
        radius = calculate_radius(cluster_points[i], center)
        assigned_points.append(cluster_points[i])
        centers.append(center)
        radii.append(radius)
    
    return centers, radii, assigned_points

def calculate_barycenter(points):
    total_x = 0
    total_y = 0
    total_weight = 0
    
    for point in points:
        total_x += point[0]
        total_y += point[1]
        total_weight += 1
    
    x_center = total_x / total_weight
    y_center = total_y / total_weight
    
    return (x_center, y_center)

def calculate_radius(points, barycenter):
    total_distance = 0
    total_weight = 0
    
    for point in points:
        distance = math.sqrt((point[0] - barycenter[0])**2 + (point[1] - barycenter[1])**2)
        total_distance += distance
        total_weight += 1
    
    average_distance = total_distance / total_weight
    
    return average_distance
