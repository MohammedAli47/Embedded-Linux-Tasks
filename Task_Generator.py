import json
import os

json_file = open(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "taskGenerator.json")
)
language_to_extension = json.load(json_file)
for i in range(len(language_to_extension["language"])):
    print(
        "%d- %s (%s)"
        % (
            i + 1,
            language_to_extension["language"][i],
            language_to_extension["extension"][i],
        )
    )

while 1:
    global task_type
    task_type = input("Task Type: ")
    if task_type.isnumeric():
        task_type = int(task_type) - 1
        try:
            language_to_extension["language"][task_type]
            break
        except IndexError:
            print("Number out of range, try another one")
    else:
        try:
            task_type = language_to_extension["language"].index(task_type.capitalize())
            break
        except:
            try:
                task_type = language_to_extension["extension"].index(task_type)
                break
            except ValueError:
                print("Incorrect option, try another one")

lecture_number = input("Lecture Number: ")
number_of_tasks = int(input("Number Of Tasks: "))
task_number_start = int(input("Task Number Start: "))
lecture_folder = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    language_to_extension["language"][task_type],
    "Lecture " + lecture_number,
)
try:
    os.makedirs(lecture_folder)
except OSError:
    print("Folder already exists, only adding new files to it")
except Exception as e:
    print(e)

task_number_counter = 0
while task_number_counter < number_of_tasks:
    with open(
        lecture_folder
        + "//Task %d.%s"
        % (
            task_number_start + task_number_counter,
            language_to_extension["extension"][task_type],
        ),
        "w",
    ) as current_file:
        # Base/Filler code
        current_file.write(language_to_extension["filler"][task_type])
    task_number_counter += 1
