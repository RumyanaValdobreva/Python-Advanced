def hot_potato(kids_names, n):
    circle = list(kids_names.split())
    while len(circle) > 1:
        for _ in range(n - 1):
            circle.append(circle.pop(0))
        removed_kid = circle.pop(0)
        print(f"Removed {removed_kid}")
    print(f"Last is {circle[0]}")


names = input()
number_of_toss = int(input())
hot_potato(names, number_of_toss)
