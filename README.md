# airflow-log-analyzer
After specifying a log folder, this program analyzes the logs available in the directory and its subdirectories. 

## Requirements:
- Python Version: 3.10.4

### Code

- To specify where this program analyzes files, copy the file path and replace the global variable provided (*LOG_DIR*). 

- The types off error messages identified can also be changed by including more error types in the *error* variable. 

## Example Output:
> Total number of errors: 3

> Here are all the errors:

> [2022-08-10 12:07:51,593] {manager.py:924} ERROR - Processor for /Users/adcv/.pyenv/versions/3.10.4/lib/python3.10/site-packages/airflow/example_dags/example_branch_operator_decorator.py exited with return code 1.

> [2022-08-10 12:07:53,170] {manager.py:924} ERROR - Processor for /Users/adcv/.pyenv/versions/3.10.4/lib/python3.10/site-packages/airflow/example_dags/example_branch_operator.py exited with return code 1.

> [2022-08-10 12:07:54,625] {manager.py:924} ERROR - Processor for /Users/adcv/.pyenv/versions/3.10.4/lib/python3.10/site-packages/airflow/example_dags/example_branch_labels.py exited with return code 1.
