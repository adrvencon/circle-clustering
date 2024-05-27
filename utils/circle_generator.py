import numpy as np

def generate_circle_points(center, radius, num_points):
    theta = np.linspace(0, 2*np.pi, num_points)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    return np.column_stack((x, y))

def generate_noisy_points(points, noise_level):
    noise = np.random.normal(0, noise_level, size=points.shape)
    return points + noise