sample={
    'name':'ffion',
    'age':13,
    'country':'england'
}

print(sample)
print(sample.keys())
print(sample.values())
print(sample['country'])

for i in sample:
    print(i,':',sample[i])

sample['area']='lincolnshire'

print(sample)

del(sample['country'])

print(sample)

sample['age']=14

print(sample)