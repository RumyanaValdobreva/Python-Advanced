n = int(input())
unique_usernames = set()

for name in range(n):
    unique_usernames.add(input())

print('\n'.join(unique_usernames))
