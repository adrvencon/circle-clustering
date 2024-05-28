from utils.csv.csv_executor import execute_tests_from_csv
from utils.csv.loader import load_test_scenario13


df = load_test_scenario13()
execute_tests_from_csv(df)