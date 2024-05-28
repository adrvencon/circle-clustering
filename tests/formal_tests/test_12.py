from utils.csv.csv_executor import execute_tests_from_csv
from utils.csv.loader import load_test_scenario12


df = load_test_scenario12()
execute_tests_from_csv(df)