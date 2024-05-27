# Circle Clustering

## Purpose
Circle Clustering is a Python project aimed at clustering a collection of points within a given range into rings. The goal is to find the best set of rings that model the given data, ensuring that all points from the cloud fit into one of those rings.

## Technologies Used
- Python
- NumPy
- Matplotlib
- Pandas

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

## Additional Information
For any additional information or questions, please refer to the project's paper.