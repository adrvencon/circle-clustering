import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import minimize

def distance_from_point_to_circle(point, center, radius):
    return abs(math.sqrt((point[0] - center[0])**2 + (point[1] - center[1])**2) - radius)

def fit_circle_to_arc(arc_points):
    # Initial guess for the center (midpoint of the arc) and radius.
    center_guess = np.mean(arc_points, axis=0)
    radius_guess = np.max(np.linalg.norm(arc_points - center_guess, axis=1))

    # Minimize the sum of distances from points to the circle to refine center and radius.
    def objective(x):
        center = x[:2]
        radius = x[2]
        return np.sum([distance_from_point_to_circle(p, center, radius) for p in arc_points])

    initial_guess = np.concatenate((center_guess, [radius_guess]))
    result = minimize(objective, initial_guess, method='Nelder-Mead')

    refined_center = result.x[:2]
    refined_radius = result.x[2]

    return refined_center, refined_radius


def generate_circle_arc(center, radius, start_angle, end_angle, num_points):
    angles = np.linspace(start_angle, end_angle, num_points)
    arc_points_x = center[0] + radius * np.cos(angles)
    arc_points_y = center[1] + radius * np.sin(angles)
    arc_points = np.column_stack((arc_points_x, arc_points_y))
    return arc_points


center = [0, 0]
radius = 5

# Define start and end angles of the arc (in radians).
start_angle = np.pi / 4
end_angle = 3 * np.pi / 4

num_points = 50
arc_points = generate_circle_arc(center, radius, start_angle, end_angle, num_points)

estimated_center, estimated_radius = fit_circle_to_arc(arc_points)

plt.figure(figsize=(8, 8))
plt.scatter(arc_points[:, 0], arc_points[:, 1], label='Arc points')
circle = plt.Circle(estimated_center, estimated_radius, color='r', fill=False, label='Fitted Circle')
plt.gca().add_patch(circle)
plt.axis('equal')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('Circle Fitting Test')
plt.legend()
plt.grid(True)
plt.show()

print("Estimated Center:", estimated_center)
print("Estimated Radius:", estimated_radius)
