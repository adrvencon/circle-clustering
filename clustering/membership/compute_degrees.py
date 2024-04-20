import numpy as np

def calculate_membership_degrees(point, clusters):
    membership_values = []

    for cluster in clusters:
        center = cluster.center
        radius = cluster.radius
        distance = np.abs(np.linalg.norm(point - center) - radius) # Using euclidean distance.
        membership_degree = 1 / (1 + distance) 
        membership_values.append(membership_degree)
    
    # Normalizing.
    total_membership = sum(membership_values)
    normalized_membership_values = [value / total_membership for value in membership_values]

    return normalized_membership_values