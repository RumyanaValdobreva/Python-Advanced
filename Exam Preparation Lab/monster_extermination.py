from collections import deque

monsters = deque(map(int, input().split(",")))
soldiers = list(map(int, input().split(",")))

monsters_killed = 0


def success(soldier, monster):
    soldier -= monster
    if not soldiers and soldier > 0:
        soldiers.append(soldier)
    elif soldiers:
        soldiers[-1] += soldier


def failure(soldier, monster):
    monster -= soldier
    monsters.append(monster)


while monsters and soldiers:
    current_monster = monsters.popleft()
    current_soldier = soldiers.pop()

    if current_soldier >= current_monster:
        monsters_killed += 1
        success(current_soldier, current_monster)
    else:
        failure(current_soldier, current_monster)

if not monsters:
    print("All monsters have been killed!")

if not soldiers:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")