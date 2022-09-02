name = 'superman'
password = 'superhero'

if name == 'superman':
    if password == 'superhero':
        print('Access granted')
else:
    print('wrong username or password')

name1 = ''
password1 = ''

while name1 != 'super' and password1 != 'superhero':
    print('please enter your name: ')
    name1 = input()
    print('please enter your password')
    password1 = input()
    # continue

    if name1 == 'super' and password1 == 'superhero':
        print('Thank you. Access granted')
    else:
        print('Access rejected.plz try again')
    continue


#print('Thank you. Access granted')
