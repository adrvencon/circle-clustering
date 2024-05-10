from utils.csv.loader import load_test_scenario1
from utils.csv.csv_executor import execute_tests_from_csv

df = load_test_scenario1()
execute_tests_from_csv(df)