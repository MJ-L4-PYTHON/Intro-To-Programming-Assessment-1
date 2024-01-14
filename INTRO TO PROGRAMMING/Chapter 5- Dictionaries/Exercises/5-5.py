pets = []

pet = {
    'animal type': 'Dog',
    'name': 'Princess',
    'owner': 'MJ',
    'weight': 30,
    'eats': 'Chicken',
}
pets.append(pet)

pet = {
    'animal type': 'Cat',
    'name': 'Leo',
    'owner': 'Trisha',
    'weight': 15,
    'eats': 'Fish',
}
pets.append(pet)

pet = {
    'animal type': 'Snake',
    'name': 'Bob',
    'owner': 'Niki',
    'weight': 10,
    'eats': 'Rats',
}
pets.append(pet)


for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))