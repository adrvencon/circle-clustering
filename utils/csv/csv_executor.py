import numpy as np
import pandas as pd
import time
from clustering.algorithm.algorithm import ring_clustering, ring_clustering_without_heuristic
from utils.clusters_plot import plot_clusters
from utils.clusters_print import print_clusters

def execute_tests_from_csv(df):
    points = df[['x', 'y']].values

    num_clusters = int(df.iloc[0]['num_clusters'])

    center_columns = [col for col in df.columns if col.startswith('center_x_') or col.startswith('center_y_')]
    radius_columns = [col for col in df.columns if col.startswith('radius_')]
    
    centers = df[center_columns].values
    radii = df[radius_columns].values

    start_time = time.time()
    # With heuristic.
    result_clusters, assigned_points, iterations = ring_clustering(points, num_clusters)
    end_time = time.time()
    elapsed_time_with_heuristic = end_time - start_time

    start_time = time.time()
    # Without heuristic.
    result_clusters_noh, assigned_points_noh, iterations_noh = ring_clustering_without_heuristic(points, num_clusters)
    end_time = time.time()
    elapsed_time_without_heuristic = end_time - start_time

    print("=================================================================")
    print("================== EXPERIMENTAL RESULTS =========================")
    print("=================================================================")
    print("NUMBER OF ITERATIONS WITH HEURISTIC: ", iterations)  
    print("ELAPSED TIME WITH HEURISTIC: ", elapsed_time_with_heuristic)
    print("NUMBER OF ITERATIONS WITHOUT HEURISTIC: ", iterations_noh)
    print("ELAPSED TIME WITHOUT HEURISTIC: ", elapsed_time_without_heuristic)
    print("------------------------------------------------------------------")
    print("------------- RESULTS WITH HEURISTIC INITIALIZATION --------------")
    print_clusters(result_clusters, assigned_points, centers[0], radii[0])
    plot_clusters(points, result_clusters)
    print("------------- RESULTS WITHOUT HEURISTIC INITIALIZATION -----------")
    print_clusters(result_clusters_noh, assigned_points_noh, centers[0], radii[0])
    plot_clusters(points, result_clusters_noh)
