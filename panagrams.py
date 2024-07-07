numbers=input('Enter the number: ')
panagram=True

numCount={
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0,
    '0':0,
}

for i in numbers:
    if i in numCount:
        numCount[i]=numCount[i]+1

for j in numCount.values():
    if j==0:
        panagram=False

if panagram==False:
    print('This is not a panagram')
else:
    print('This is a panagram')