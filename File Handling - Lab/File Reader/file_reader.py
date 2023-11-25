import os

WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIRECTORY_PATH, "numbers.txt")

file = open(file_path, "r")

total_sum = 0

for line in file:
    current_num = int(line)
    total_sum += current_num

print(total_sum)