import numpy as np
import pandas as pd
from utils.circle_generator import generate_circle_points, generate_noisy_points

test_scenarios = [
    {"description": "One circle, low noise",
     "circle_params": [{"center": (1, 2), "radius": 3, "num_points": 80}],
     "noise_level": 0.1,
     "num_clusters": 1},
    {"description": "One circle, high noise",
     "circle_params": [{"center": (1, 2), "radius": 3, "num_points": 80}],
     "noise_level": 0.4,
     "num_clusters": 1},
    {"description": "Two circles, close together, low noise",
     "circle_params": [{"center": (1, 2), "radius": 2, "num_points": 60},
                       {"center": (3, 3), "radius": 2, "num_points": 60}],
     "noise_level": 0.1,
     "num_clusters": 2},
    {"description": "Two circles, overlapping, high noise",
     "circle_params": [{"center": (1, 1), "radius": 3, "num_points": 80},
                       {"center": (2.5, 2.5), "radius": 3, "num_points": 80}],
     "noise_level": 0.4,
     "num_clusters": 2},
    {"description": "Two circles, distant, high noise",
     "circle_params": [{"center": (1, 1), "radius": 3, "num_points": 80},
                       {"center": (15, 15), "radius": 3, "num_points": 80}],
     "noise_level": 0.4,
     "num_clusters": 2},
    {"description": "Two circles, distant, low noise",
     "circle_params": [{"center": (5, 5), "radius": 4, "num_points": 120},
                       {"center": (15, 15), "radius": 4, "num_points": 120}],
     "noise_level": 0.1,
     "num_clusters": 2},
        {"description": "Three circles, close together, medium noise",
     "circle_params": [{"center": (2, 2), "radius": 2, "num_points": 60},
                       {"center": (6, 6), "radius": 2.5, "num_points": 70},
                       {"center": (10, 10), "radius": 3, "num_points": 80}],
     "noise_level": 0.2,
     "num_clusters": 3},
         {"description": "Three circles, separate, medium noise",
     "circle_params": [{"center": (1, 1), "radius": 2, "num_points": 50},
                       {"center": (5, 5), "radius": 2, "num_points": 50},
                       {"center": (9, 9), "radius": 2, "num_points": 50}],
     "noise_level": 0.2,
     "num_clusters": 3},
    {"description": "Three circles, close together, high noise",
     "circle_params": [{"center": (1, 1), "radius": 1.5, "num_points": 40},
                       {"center": (2.5, 2.5), "radius": 1.5, "num_points": 40},
                       {"center": (4, 4), "radius": 1.5, "num_points": 40}],
     "noise_level": 0.4,
     "num_clusters": 3},
    {"description": "Four circles, varying sizes, low noise",
     "circle_params": [{"center": (1, 2), "radius": 2, "num_points": 60},
                       {"center": (4, 4), "radius": 1.5, "num_points": 60},
                       {"center": (7, 7), "radius": 3, "num_points": 80},
                       {"center": (10, 10), "radius": 2.5, "num_points": 70}],
     "noise_level": 0.1,
     "num_clusters": 4}
]

for i, scenario in enumerate(test_scenarios):
    points = np.concatenate([generate_circle_points(**params) for params in scenario["circle_params"]])
    noisy_points = generate_noisy_points(points, scenario["noise_level"])
    df = pd.DataFrame(noisy_points, columns=["x", "y"])
    df["num_clusters"] = scenario["num_clusters"]
    df.to_csv(f"test_scenario_{i+1}.csv", index=False)
