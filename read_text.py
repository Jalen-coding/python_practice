file=input('What file would you like for me to open: ')

sent=[]
try:
    with open(file) as f:
        sent=[word.rstrip() for word in f]

except FileNotFoundError:
    print('file does not exist')
    exit()

words=[]
for s in sent:
    s=s.split(' ')
    words.append(s)

num_char=0
num_words=0
num_lines=0
for i in words:
    num_lines+=1
    for j in i:
        num_words+=1
        for k in j:
            num_char+=1

print('Number of characters:',num_char)
print('Number of words:',num_words)
print('Number of lines:',num_lines)
