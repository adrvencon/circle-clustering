from utils.csv.csv_executor import execute_tests_from_csv
from utils.csv.loader import load_test_scenario6


df = load_test_scenario6()
execute_tests_from_csv(df)