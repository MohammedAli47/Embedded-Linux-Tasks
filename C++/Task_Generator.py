import os
lecture_number = int(input("Lecture Number: "))
number_of_tasks = int(input("Number Of Tasks: "))
task_number_start = int(input("Task Number Start: "))
task_number_counter = 0
dir = os.path.dirname(os.path.realpath(__file__))
while task_number_counter < number_of_tasks:
    with open(dir + "//Lecture %d Task %d.cpp" % (lecture_number, (task_number_start + task_number_counter)), "w") as current_file:
        current_file.write("#include <iostream>\nint main() {\n\t\n\treturn 0;\n}")
    task_number_counter += 1
