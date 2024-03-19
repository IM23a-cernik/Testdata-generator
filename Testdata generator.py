from faker import Faker
def menu():
    name = input('Dateinamen auswählen\n')
    place = input('Wählen sie das Land aus:\nde, en_US, en_UK\n')
    fake = Faker(place)
    choice = input('Wählen Sie den Generator:\nPerson: P\n')
    if choice == 'p' or 'P':
        person(name, fake)
def person(name, fake):
    id = 0
    amount = int(input('Wieviele Einträge wollen Sie?\n'))
    with open(f'{name}.txt', 'w') as file:
        for i in range(0, amount):
            first_name = fake.first_name()
            if 'ä' in first_name:
                first_name = first_name.replace("ä", "ae")
            elif 'ü' in first_name:
                first_name = first_name.replace("ü", "ue")
            elif 'ö' in first_name:
                first_name = first_name.replace("ö", "oe")
            elif 'ß' in first_name:
                first_name = first_name.replace("ß", "ss")
            last_name = fake.last_name()
            if 'ä' in last_name:
                last_name = last_name.replace("ä", "ae")
            elif 'ü' in last_name:
                last_name = last_name.replace("ü", "ue")
            elif 'ö' in last_name:
                last_name = last_name.replace("ö", "oe")
            elif 'ß' in last_name:
                last_name = last_name.replace("ß", "ss")
            file.write(f'{id + 1},{first_name},{last_name},{fake.postcode()}\n')
            id += 1

if __name__ == '__main__':
    menu()