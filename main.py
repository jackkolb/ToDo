#Todo: A service to manage things to do

import sys
import difflib
import os 

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"

def new_task():
    task = " ".join(sys.argv[2:]) + "\n"
    with open(dir_path + "tasks", "a") as tasks_file:
        tasks_file.write(task)
    retrieve_tasks()
    return


def retrieve_tasks():
    print("Tasks:")
    with open(dir_path + "tasks", "r") as tasks_file:
        lines = tasks_file.readlines()
        for line in lines:
            print(line[:-1])
    return


def remove_task():
    task = " ".join(sys.argv[2:]) + "\n"
    with open(dir_path + "tasks", "r") as tasks_file:
        lines = tasks_file.readlines()
    close_matches = difflib.get_close_matches(task, lines)

    if len(close_matches) == 0:
        print("No close matches")
        return
    
    closest_match = close_matches[0]
    print("Closest Match: " + closest_match[:-1])
    lines.remove(closest_match)
    with open(dir_path + "tasks", "w") as tasks_file:
        [tasks_file.write(line) for line in lines]
    print("Task \"" + closest_match[:-1] + "\" removed!")
    retrieve_tasks()
    return


if __name__ == "__main__":
    if len(sys.argv) < 2:
        retrieve_tasks()
        sys.exit() 
    command = sys.argv[1].lower()
    valid_commands = ["new", "add", "done", "remove"]
    if command not in valid_commands:
        print("A valid command is required: add, remove")
        retrieve_tasks()

    if command == "new" or command == "add" or command == "a":
        new_task()
    if command == "done" or command == "remove" or command == "r":
        remove_task()
    sys.exit()
