number_of_reservations = int(input())
reservations = set()

for line in range(number_of_reservations):
    reservation_number = input()
    reservations.add(reservation_number)

while True:
    command = input()
    if command == 'END':
        break
    reservations.remove(command)

print(len(reservations))

for reserv in sorted(reservations):
    print(reserv)