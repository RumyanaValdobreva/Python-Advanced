from collections import deque

tools_value = deque([int(x) for x in input().split()])
substances = list(map(int, input().split()))
challenges = list(map(int, input().split()))


def resolved(current_sum):
    challenges.remove(current_sum)


def not_resolved(current_tool, current_substance):
    current_tool += 1
    tools_value.append(current_tool)
    current_substance -= 1
    if current_substance > 0:
        substances.append(current_substance)


while tools_value and substances and challenges:
    current_tool = tools_value.popleft()
    current_substance = substances.pop()
    current_sum = current_tool * current_substance

    if current_sum in challenges:
        resolved(current_sum)
    else:
        not_resolved(current_tool, current_substance)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools_value:
    print(f"Tools: {', '.join(str(x) for x in tools_value)}")

if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")

if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")