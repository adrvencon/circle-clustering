from utils.csv.csv_executor import execute_tests_from_csv
from utils.csv.loader import load_test_scenario5


df = load_test_scenario5()
execute_tests_from_csv(df)