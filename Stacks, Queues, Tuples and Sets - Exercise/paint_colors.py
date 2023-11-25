from collections import deque

colors = deque(input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = {"orange": ["red", "yellow"],
                    "purple": ["red", "blue"],
                    "green": ["blue", "yellow"]}

collected_colors = []

while colors:
    first = colors.popleft()
    second = colors.pop() if colors else ""
    if first + second in main_colors or first + second in secondary_colors:
        collected_colors.append(first + second)
    elif second + first in main_colors or second + first in secondary_colors:
        collected_colors.append(second + first)
    else:
        if len(first) > 1:
            colors.insert(len(colors) // 2, first[:-1])
        if len(second) > 1:
            colors.insert(len(colors) // 2, second[:-1])


for color in collected_colors:
    if color in secondary_colors:
        for c in secondary_colors[color]:
            if c not in collected_colors:
                collected_colors.remove(color)
                break


print(collected_colors)
