import numpy as np
import pandas as pd
from utils.circle_generator import generate_circle_points, generate_noisy_points

test_scenarios = [
    {"description": "One circumference, no noise",
     "circle_params": [{"center": (1, 2), "radius": 3, "num_points": 40}],
     "noise_level": 0.0,
     "num_clusters": 1},
    {"description": "One circumference, low noise",
     "circle_params": [{"center": (1, 2), "radius": 3, "num_points": 40}],
     "noise_level": 0.1,
     "num_clusters": 1},
    {"description": "One circumference, high noise",
     "circle_params": [{"center": (1, 2), "radius": 3, "num_points": 40}],
     "noise_level": 0.2,
     "num_clusters": 1},
    {"description": "Two circumferences, separated, no noise",
     "circle_params": [{"center": (0, 0), "radius": 1, "num_points": 40},
                       {"center": (3, 3), "radius": 1.5, "num_points": 40}],
     "noise_level": 0.0,
     "num_clusters": 2},
    {"description": "Two circumferences, separated, low noise",
     "circle_params": [{"center": (0, 0), "radius": 1, "num_points": 40},
                       {"center": (3, 3), "radius": 1.5, "num_points": 40}],
     "noise_level": 0.1,
     "num_clusters": 2},
    {"description": "Two circumferences, separated, high noise",
     "circle_params": [{"center": (0, 0), "radius": 1, "num_points": 40},
                       {"center": (3, 3), "radius": 1.5, "num_points": 40}],
     "noise_level": 0.2,
     "num_clusters": 2},
        {"description": "Two circumferences, overlapping, no noise",
     "circle_params": [{"center": (1, 2), "radius": 2, "num_points": 40},
                       {"center": (3, 3), "radius": 2, "num_points": 40}],
     "noise_level": 0.0,
     "num_clusters": 2},
    {"description": "Two circumferences, overlapping, low noise",
     "circle_params": [{"center": (1, 2), "radius": 2, "num_points": 40},
                       {"center": (3, 3), "radius": 2, "num_points": 40}],
     "noise_level": 0.1,
     "num_clusters": 2},
    {"description": "Two circumferences, overlapping, high noise",
     "circle_params": [{"center": (1, 2), "radius": 2, "num_points": 40},
                       {"center": (3, 3), "radius": 2, "num_points": 40}],
     "noise_level": 0.2,
     "num_clusters": 2},
    {"description": "Two circumferences, concentric, no noise",
     "circle_params": [{"center": (1, 1), "radius": 3, "num_points": 40},
                       {"center": (1, 1), "radius": 1, "num_points": 40}],
     "noise_level": 0.0,
     "num_clusters": 2},
    {"description": "Two circumferences, concentric, low noise",
     "circle_params": [{"center": (1, 1), "radius": 3, "num_points": 40},
                       {"center": (1, 1), "radius": 1, "num_points": 40}],
     "noise_level": 0.1,
     "num_clusters": 2},
    {"description": "Two circumferences, concentric, high noise",
     "circle_params": [{"center": (1, 1), "radius": 3, "num_points": 40},
                       {"center": (1, 1), "radius": 1, "num_points": 40}],
     "noise_level": 0.2,
     "num_clusters": 2},
    {"description": "Three circumferences, separated, no noise",
     "circle_params": [{"center": (0, 0), "radius": 1, "num_points": 40},
                       {"center": (3, 3), "radius": 0.5, "num_points": 40},
                       {"center": (5, 5), "radius": 1, "num_points": 40}],
     "noise_level": 0.0,
     "num_clusters": 3},
    {"description": "Three circumferences, separated, low noise",
     "circle_params": [{"center": (0, 0), "radius": 1, "num_points": 40},
                       {"center": (3, 3), "radius": 0.5, "num_points": 40},
                       {"center": (5, 5), "radius": 1, "num_points": 40}],
     "noise_level": 0.1,
     "num_clusters": 3},
    {"description": "Three circumferences, separated, high noise",
     "circle_params": [{"center": (0, 0), "radius": 1, "num_points": 40},
                       {"center": (3, 3), "radius": 0.5, "num_points": 40},
                       {"center": (5, 5), "radius": 1, "num_points": 40}],
     "noise_level": 0.2,
     "num_clusters": 3},
]

for i, scenario in enumerate(test_scenarios):
    points = np.concatenate([generate_circle_points(**params) for params in scenario["circle_params"]])
    noisy_points = generate_noisy_points(points, scenario["noise_level"])
    df = pd.DataFrame(noisy_points, columns=["x", "y"])
    df["num_clusters"] = scenario["num_clusters"]
    for j, circle_param in enumerate(scenario["circle_params"]):
        center_x, center_y = circle_param["center"]
        radius = circle_param["radius"]
        df[f"center_x_{j+1}"] = center_x
        df[f"center_y_{j+1}"] = center_y
        df[f"radius_{j+1}"] = radius
    df.to_csv(f"test_scenario_{i+1}.csv", index=False)
