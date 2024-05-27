from utils.csv.loader import load_test_scenario3
from utils.csv.csv_executor import execute_tests_from_csv

df = load_test_scenario3()
execute_tests_from_csv(df)