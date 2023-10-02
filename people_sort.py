#dictionary of people
people={}

#get user input
run=True
while run:

    name=input('\nenter a name: ')
    name=name.capitalize()
    age=int(input('\nenter an age: '))
    
    people[name]=age
    
    more_names=input('\nEnter more or no\ny or n: ')

    if more_names=='n':
        run=False
    elif more_names=='y':
        run=True
    else:
        print('\nThat is not an option')
        more_names=input('\ny or n: ')
print('Original list:',people)

#bubble sort algorithm
key=list(people.keys())
val=list(people.values())

#sort by names
for j in range(len(key)):
    for i in range(len(key)-1):
        if key[i]>key[i+1]:
            key[i],val[i],key[i+1],val[i+1]=key[i+1],val[i+1],key[i],val[i]

print('\nSorted by names:')
for i in key:
    print(i,':',people[i])

#sort by ages
for j in range(len(val)):
    for i in range(len(val)-1):
        if val[i]<val[i+1]:
            val[i],key[i],val[i+1],key[i+1]=val[i+1],key[i+1],val[i],key[i]
print('\nSorted by ages:')
for i in key:
    print(i,':',people[i])
