# Circle Clustering

## Purpose
Circle Clustering is a Python project aimed at clustering a collection of points within a given range into rings. The goal is to find the best set of rings that model the given data, ensuring that all points from the cloud fit into one of those rings.

## Technologies Used
- Python
    - NumPy
    - Matplotlib
    - Pandas
    - Time
    - Scipy
    - Os

## Setup Instructions
To set up the project environment, follow these steps:
1. Clone the repository to your local machine.
2. Navigate to the project's root directory in your console.
3. Set the PYTHONPATH environment variable to include the project root. Replace `<your_project_root>` with the path to your project's root directory.
    ```
    $env:PYTHONPATH = "<your_project_root>;$env:PYTHONPATH"
    ```

## Running Tests
To execute the tests for the Circle Clustering project, follow these instructions:
1. Navigate to the `tests` directory.
2. Inside the `tests` directory, you'll find two subdirectories:
   - `formal_tests`: Contains formal tests that were included in the project's paper.
   - `informal_tests`: Contains informal tests used during development.
3. In the `formal_tests` directory, you'll find multiple test files. Each file represents one test scenario.
4. To execute a single test, simply run the corresponding test file.
5. To execute all formal tests at once, run the `all.py` file.

## Creating Test Cases
To create new test cases for the project, follow these instructions:
1. Navigate to the `utils` directory.
2. Inside the `utils` directory, you'll find the `csv` subdirectory.
3. In the `csv` directory, you'll find three files: `csv_executor.py`, `csv_generator.py`, and `loader.py`.

4. In the `csv_generator.py` file, you can introduce your new test case. You can either replace an existing test case or add a new test case (recommended). To insert a new test case, replace the placeholders with the specific details of your test case, adding the following code snippet to `csv_generator.py`.
```
{"description": "<Description of your test case>",
"circle_params": [{"center": (<x-coordinate>, <y-coordinate>), "radius": <radius>, "num_points": <number_of_points>}],
"noise_level": <noise_level>,
"num_clusters": <number_of_clusters>}
```

6. Execute `csv_generator.py`. A new CSV file should be created, or a previous one should appear as modified if an old test case was altered instead.

5. Your new test will automatically be included in the `all.py` file. If you wish to run it separately, you'll have to create a file for it in the `formal_tests` directory. To execute your newly created test case, you only need to copy-paste and replace <your_scenario_number> with the number of your newly generated test case in the following code snippet. This number should correspond to the csv file generated in step 6.
```
test_scenarios = load_test_scenarios()
scenario_number = <your_scenario_number>
scenario_name = f"test_scenario_{scenario_number}"
scenario_df = test_scenarios[scenario_name]
execute_tests_from_csv(scenario_df)
```

7. You can now execute your new test cases by following the steps in the [previous section](#running-tests).

**For examples, please consult the already-made tests in the codebase (1-15).**

## Additional Information
For any additional information or questions, please refer to the project's paper.