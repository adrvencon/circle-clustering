from utils.csv.loader import load_test_scenario4
from utils.csv.csv_executor import execute_tests_from_csv

df = load_test_scenario4()
execute_tests_from_csv(df)