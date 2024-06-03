from utils.csv.csv_executor import execute_tests_from_csv
from utils.csv.loader import load_test_scenarios

test_scenarios = load_test_scenarios()

for scenario_name, df in test_scenarios.items():
    execute_tests_from_csv(df)
