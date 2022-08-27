
print ("Enter Marks: ")
marks = int(input())

if marks > 0 and 32:
    print('Invalid Marks')

elif marks <33 and 40:
    print('Grade D')
elif marks < 41 and 49:
    print('Grade C')

elif marks < 50 and 59:
    print('Grade B')

elif marks < 60 and 69:
    print('Grade A-')

elif marks < 70 and 79:
    print('Grade A')

elif marks < 80 and 100:
    print('Grade A+')

else:
    print("Invalid Marks")
