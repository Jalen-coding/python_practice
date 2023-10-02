#get user input
run=True
while run:
    words=input('Enter as many words as you would like and press enter when you are done.\n')
    if words=='':
        print('NO input recieved')
        exit()
    run=False
#split every letter from the string and get rid of spaces
letters=[]
for i in words:
    if i ==' ':
        pass
    else:
        letters.append(i)
letter=0
for i in letters:
    letter+=1
print(letter)

#split all words
words=words.split()
for j in range(len(words)):
    for i in range(len(words)-1):
        if words[i]>words[i+1]:
            words[i],words[i+1]=words[i+1],words[i]
print("Words in sorted order")
print(words)
