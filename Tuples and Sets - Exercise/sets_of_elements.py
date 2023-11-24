n, m = (int(x) for x in input().split())

set_n = set()
set_m = set()

for line in range(n):
    set_n.add(input())

for line in range(m):
    set_m.add(input())

common_elements = set_n.intersection(set_m)

print("\n".join(common_elements))