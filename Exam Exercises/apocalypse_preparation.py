# Python Advanced Exam - 18 February 2023

from collections import deque

textile = deque([int(x) for x in input().split()])
medicament = list(map(int, input().split()))

healing_items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while True:
    if not textile and not medicament:
        print("Textiles and medicaments are both empty.")
        break
    if not textile:
        print("Textiles are empty.")
        break
    if not medicament:
        print("Medicaments are empty.")
        break

    current_textile = textile.popleft()
    current_medicament = medicament.pop()
    result = current_textile + current_medicament

    if result == 30:
        healing_items["Patch"] += 1
    elif result == 40:
        healing_items["Bandage"] += 1
    elif result == 100:
        healing_items["MedKit"] += 1
    elif result > 100:
        healing_items["MedKit"] += 1
        result -= 100
        medicament[-1] += result
    else:
        current_medicament += 10
        medicament.append(current_medicament)

for key, value in sorted(healing_items.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    if int(value) > 0:
        print(f"{key} - {value}")

if textile:
    print(f"Textiles left: {', '.join(map(str, textile))}")

if medicament:
    medicament.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicament))}")