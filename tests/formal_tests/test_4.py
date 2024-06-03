from utils.csv.loader import load_test_scenarios
from utils.csv.csv_executor import execute_tests_from_csv

# COMMENT: Please use this as a template for executing your tests individually. If all previous steps are performed
# correctly, you should only need to change the scenario_number to your new test case to execute the test.

test_scenarios = load_test_scenarios()
scenario_number = 4
scenario_name = f"test_scenario_{scenario_number}"
scenario_df = test_scenarios[scenario_name]
execute_tests_from_csv(scenario_df)