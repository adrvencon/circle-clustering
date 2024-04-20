import numpy as np

from clustering.circlefit.circle_fit_weighted import fit_circle_weighted
from clustering.datamodel.cluster import Cluster
from clustering.membership.compute_degrees import calculate_membership_degrees
from utils.transpose_list import transpose_list_of_lists

def initialize_clusters(num_clusters, points):
    centers = []
    
    # Randomly select the first center from the data points.
    initial_center = points[np.random.choice(len(points))]
    centers.append(initial_center)
    
    for _ in range(1, num_clusters):
        # Compute the distance from each point to the nearest center.
        distances = np.array([np.min([np.linalg.norm(point - center) for center in centers]) for point in points])
        probabilities = distances ** 2 / np.sum(distances ** 2)
        next_center = points[np.random.choice(len(points), p=probabilities)]
        centers.append(next_center)
    
    clusters = [Cluster(center, 0) for center in centers]
    return clusters

def update_clusters(points, clusters):
    new_centers, new_radii = fit_circle_weighted(points, clusters)
    for i in range(len(clusters)):
        cluster = clusters[i]
        new_center = new_centers[i]
        new_radius = new_radii[i]
        cluster.update_center_radius(new_center, new_radius)

def update_membership_degrees(points, clusters):
    membership_degrees = transpose_list_of_lists([calculate_membership_degrees(point, clusters) for point in points])
    for i in range(len(clusters)):
        cluster = clusters[i]
        cluster.update_membership_degree(membership_degrees[i])

def ring_clustering(points, num_clusters, max_iterations=5000, tol=1e-8):
    clusters = initialize_clusters(num_clusters, points)
    
    prev_centers = [cluster.center for cluster in clusters]
    
    for _ in range(max_iterations):
        update_membership_degrees(points, clusters)
        update_clusters(points, clusters)
        
        new_centers = [cluster.center for cluster in clusters]
        
        # Check convergence.
        center_movement = max(np.linalg.norm(np.array(new_center) - np.array(prev_center)) for new_center, prev_center in zip(new_centers, prev_centers))
        if center_movement < tol:
            break
        
        prev_centers = new_centers
    
    return clusters

