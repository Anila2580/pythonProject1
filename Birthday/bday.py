birthdays = {'Alice': 'Apr 1', 'Bob': 'May 1', 'Batman': 'mar 1'}

while True:
    print('please enter your name: ')
    name = input()
    name1 = name.title()

    if name1 == ' ':
        print('please enter your name')
    else:

        if name1 in birthdays:
            print(birthdays[name1] + ' is your birthday')

        else:
            print('you dont have birthday')

    continue
