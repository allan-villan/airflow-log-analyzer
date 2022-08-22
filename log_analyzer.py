from pathlib import Path

LOG_DIR = "/Users/adcv/airflow/logs"

def analyze_file(file_list):
    error_count = 0
    error_messages = []

    for file in file_list:
        current_file = open(str(file), "r")

        for line in current_file.readlines():
            contents = line.split(" ")
            for word in contents:
                if word in error:
                    error_messages.append(line)
                    error_count += 1

    return error_count, error_messages


file_list = Path(LOG_DIR).rglob("*.log")
error = ["ERROR"]

count, cur_list = analyze_file(file_list)
print("Total number of errors: " + str(count))
print("Here are all the errors:")
for error in cur_list:
    print(error)