import pandas as pd
import os

def load_test_scenarios():
    test_scenarios = {}
    root_folder = '.' 
    
    for file_name in os.listdir(root_folder):
        if file_name.endswith('.csv'):
            scenario_name = file_name.split('.')[0]
            test_scenarios[scenario_name] = pd.read_csv(os.path.join(root_folder, file_name))
    
    return test_scenarios