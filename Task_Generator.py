lecture_number = int(input("Lecture Number: "))
number_of_tasks = int(input("Number Of Tasks: "))
task_number_start = int(input("Task Number Start: "))
task_number_counter = 0
while task_number_counter < number_of_tasks:
    with open("Lecture %d Task %d.py" % (lecture_number, (task_number_start + task_number_counter)), "w") as current_file:
        current_file.write("import os\nimport sys\n\n")
    task_number_counter += 1
