car = {'make': 'bmw',
       'model': 'bw22',
       'year': 2022
       }

# Nested Dictionary

User = {'Name': "Smith",
        'age': 30,
        'location': {
            'present_address': {'road': '01', 'house': '002'},
            'permanent_address': 'ctg'

        }
        }

person = {'First_name': 'Najia', "last_name": 'Hossain', 'age': 26, 'city': 'Dhaka'}

print(car)
print(car['model'])
print(User['location']['present_address']['road'])
print(car.values())
print(person['city'])

fav_clr = {'smith': 'Red',
           'kevin': 'blue',
           'devid': 'green'}

for name in fav_clr.keys():
    print(name.title())

for color in fav_clr.values():
    print(color.title())

for name, color in fav_clr.items():
    print(f"{name.title()}'s favorite color is {color.title()}.")


