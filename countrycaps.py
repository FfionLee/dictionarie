world={}

print('1. Insert\n2. Display all countries\n3. Display all capitals\n4. Get capital\n5. Delete')

while True:
    choice=int(input('Enter your choice (1-5): '))

    if choice==1:
        country=input('Enter country: ')
        capital=input('Enter capital: ')
        world[country]=capital
    elif choice==2:
        print(list(world.keys()))
    elif choice==3:
        print(list(world.values()))
    elif choice==4:
        country=input('Enter country: ')
        print(world[country])
    elif choice==5:
        country=input('Enter country: ')
        del(world[country])
    else:
        break