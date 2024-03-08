
# Without walrus operator

cars=list()
while True:
    car=input('Enter your fav car names:')
    if car == 'quit':
        break

    cars.append(car)
print(cars)
     
  


# Using Walrus Opeator

cars=list()

while(car:= input('Enter fav cars name:'))!= 'quit':
    cars.append(car)
    
print(cars)