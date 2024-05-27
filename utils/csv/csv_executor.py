import numpy as np
import pandas as pd
import ast
from clustering.algorithm.algorithm import ring_clustering
from utils.clusters_plot import plot_clusters
from utils.clusters_print import print_clusters

def execute_tests_from_csv(df):
    points = df[['x', 'y']].values

    num_clusters = int(df.iloc[0]['num_clusters'])

    result_clusters, assigned_points = ring_clustering(points, num_clusters)

    print_clusters(result_clusters, assigned_points)
    plot_clusters(points, result_clusters)
