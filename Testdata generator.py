from faker import Faker
name = input('Namen auswählen\n')
fake = Faker()
id = 0
amount = int(input('How many entries do you want?\n'))
with open(f'{name}.txt', 'w') as file:
    for i in range(0, amount):
        file.write(f'{id + 1}, {fake.first_name()}, {fake.last_name()}\n')
        id += 1