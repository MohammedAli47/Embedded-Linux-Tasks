import json
import os

json_file = open(".vscode//taskGenerator.json")
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
task_type = input("Task Type: ")
lecture_number = input("Lecture Number: ")
number_of_tasks = int(input("Number Of Tasks: "))
task_number_start = int(input("Task Number Start: "))
if task_type.isnumeric():
    task_type = int(task_type) - 1
else:
    task_type = language_to_extension["language"].index(task_type.capitalize())
lecture_folder = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    language_to_extension["language"][task_type],
    "Lecture " + lecture_number,
)
try:
    os.makedirs(lecture_folder)
except Exception as e:
    print(e)
    print("Folder already exists, only adding new files to it")
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
