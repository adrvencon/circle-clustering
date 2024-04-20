import matplotlib.pyplot as plt
import numpy as np
import math

def fit_circle(points):
    center = calculate_barycenter(points)
    radius = calculate_radius(points, center)
    return center, radius

def calculate_barycenter(points):
    total_x = 0
    total_y = 0
    num_points = len(points)
    
    for point in points:
        total_x += point[0]
        total_y += point[1]
    
    x_center = total_x / num_points
    y_center = total_y / num_points
    
    return (x_center, y_center)


def calculate_radius(points, barycenter):
    total_distance = 0
    num_points = len(points)
    for point in points:
        distance = math.sqrt((point[0] - barycenter[0])**2 + (point[1] - barycenter[1])**2)
        total_distance += distance
    
    average_distance = total_distance / num_points
    
    return average_distance

np.random.seed(0)
num_points = 100
radius_true = 2
center_true = [10, 10]
theta = np.linspace(0, 2*np.pi, num_points)
points_x = center_true[0] + radius_true * np.cos(theta) + np.random.normal(0, 0.5, num_points)
points_y = center_true[1] + radius_true * np.sin(theta) + np.random.normal(0, 0.5, num_points)
points = np.column_stack((points_x, points_y))

estimated_center, estimated_radius = fit_circle(points)

plt.figure(figsize=(8, 8))
plt.scatter(points[:, 0], points[:, 1], label='Data points')
circle = plt.Circle(estimated_center, estimated_radius, color='r', fill=False, label='Fitted Circle')
plt.gca().add_patch(circle)
plt.axis('equal')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('Circle Fitting Test')
plt.legend()
plt.grid(True)
plt.show()

print("True Center:", center_true)
print("True Radius:", radius_true)
print("Estimated Center:", estimated_center)
print("Estimated Radius:", estimated_radius)