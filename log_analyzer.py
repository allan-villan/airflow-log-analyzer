from pathlib import Path

LOG_DIR = "/Users/adcv/airflow/logs"

def analyze_file(file_list: str):
"""
    The analyze_file method is the main method of this script. 
    
"""
    error_count = 0
    error_messages = []

    for file in file_list:
        current_file = open(str(file), "r")

        for line in current_file.readlines():
            contents = line.split(" ") # delimiter in logs are spaces
            for word in contents:
                if word in error:
                    error_messages.append(line)
                    error_count += 1

    # as specified in requirements
    return error_count, error_messages

# grabs every .log file in Path specified
file_list = Path(LOG_DIR).rglob("*.log")
# can include more errors in this variable
# ex: ["ERROR","WARNING"]
error = ["ERROR"]

#as specified in requirements
count, cur_list = analyze_file(file_list)

print("Total number of errors: " + str(count))
print("Here are all the errors:")
for error in cur_list:
    print(error)
