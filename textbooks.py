textbooks={
    'maths':'£15.00',
    'history':'£17.00',
    'relgion':'£14.00',
    'physics':'£10.00',
}

textbooks['physics']='£20.00'

textbooks['geography']='£16.00'
textbooks['english']='£13.00'

book=input('Enter textbook: ')
print(textbooks[book])

for i in textbooks:
    print(i,':',textbooks[i])