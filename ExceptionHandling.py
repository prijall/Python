a= int(input('Enter the number:'))
print(f'Multiplication table of {a} is:')

try:
    for i in range(1, 11):
        print(f'{a} x {i}= {a*i}')
except:
    print("Invalid Input")

print('this code is ended')