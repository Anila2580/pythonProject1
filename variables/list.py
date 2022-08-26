student1 = 'najia'
email = 'najia@gmail.com'
phone = '12345678'
address = 'dhaka'

student2 = 'najia'
email = 'najia@gmail.com'
phone = '12345678'
address = 'dhaka'

student1 = ['najia', 'najia@gmail.com', '1234578', 'dhaka']
student2 = ['anila', 'anila@gmail.com', '1234578', 'dhaka']
print(student1)
print(student1[1])
print(len(student1))

student2_name = student2[0]
print(student2_name)

guest = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print('for lunch')
print(guest[0], guest[1], guest[2], guest[3], guest[4])
print('for dinner')
print(guest[5], guest[6], guest[7], guest[8], guest[9])

lunch = guest[0:5]  # 0 is a index and 5 is a position
print(lunch)

dinner = guest[5:]
print(dinner)

special_guest = guest[2:4]
print(special_guest)

number = [12, 1, 5, 4, 6, 285, 3, 0]
number.sort()
print(number)
number.reverse()
print(number)

number.insert(3, 10)
print(number)

number.remove(number[2])
print(number)
number.pop(0)
print(number)
number.remove(4)
print(number)

number.append(100)
print(number)
number.clear()
print(number)

