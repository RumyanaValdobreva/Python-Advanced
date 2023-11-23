number_of_cars = int(input())
cars = set()

for line in range(number_of_cars):
    command, car_number = input().split(', ')
    if command == 'IN':
        cars.add(car_number)
    elif command == 'OUT':
        cars.remove(car_number)

if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")