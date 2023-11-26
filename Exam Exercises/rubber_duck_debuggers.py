# Python Advanced Retake Exam - 12 April 2023

from collections import deque

programmers_time = deque([int(x) for x in input().split()])
number_of_tasks = list(map(int, input().split()))
ducks_info = {"Darth Vader Ducky": 0, "Thor Ducky": 0,
              "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}

while programmers_time and number_of_tasks:
    current_time = programmers_time.popleft()
    current_task = number_of_tasks.pop()

    result = current_time * current_task

    if 0 <= result <= 60:
        ducks_info["Darth Vader Ducky"] += 1
    elif 61 <= result <= 120:
        ducks_info["Thor Ducky"] += 1
    elif 121 <= result <= 180:
        ducks_info["Big Blue Rubber Ducky"] += 1
    elif 181 <= result <= 240:
        ducks_info["Small Yellow Rubber Ducky"] += 1
    else:
        programmers_time.append(current_time)
        number_of_tasks.append(current_task - 2)

if not programmers_time and not number_of_tasks:
    print("Congratulations, all tasks have been completed! Rubber ducks rewarded: ")

for key, value in ducks_info.items():
    print(f"{key}: {value}")