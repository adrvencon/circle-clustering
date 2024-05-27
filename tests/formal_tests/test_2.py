from utils.csv.loader import load_test_scenario2
from utils.csv.csv_executor import execute_tests_from_csv

df = load_test_scenario2()
execute_tests_from_csv(df)