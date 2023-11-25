def accommodate_new_pets(capacity, max_kg, *args):
    accommodated_pets = {}
    output = ""

    for pet_type, pet_kg in args:
        if capacity <= 0:
            output += 'You did not manage to accommodate all pets!\n'
            break

        if pet_kg > max_kg:
            continue

        if pet_type not in accommodated_pets:
            accommodated_pets[pet_type] = 0
        accommodated_pets[pet_type] += 1
        capacity -= 1

    else:
        output += f"All pets are accommodated! Available capacity: {capacity}.\n"

    output += "Accommodated pets:\n"

    for pet_type, pet_number in sorted(accommodated_pets.items()):
        output += f"{pet_type}: {pet_number}\n"

    return output