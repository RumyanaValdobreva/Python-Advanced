import os

command = input()

while command != 'End':
    # command, file_name, *args = input().split('-')
    line = command.split("-")
    command = line[0]
    file_name = line[1]
    if command == 'Create':
        open(file_name, "w").close()
    elif command == 'Add':
        content = line[2]
        with open(file_name, "a") as file:
            file.write(f"{content}" + "\n")
    elif command == 'Replace':
        old_string = line[2]
        new_string = line[3]
        try:
            with open(file_name, "r") as file:
                content_of_file = file.read()
            with open(file_name, "w") as file:
                content_of_file = content_of_file.replace(old_string, new_string)
                file.write(content_of_file)
        except FileNotFoundError:
            print("An error occurred")
    elif command == 'Delete':
        try:
            os.remove(f"{file_name}")
        except FileNotFoundError:
            print("An error occurred")
    command = input()