n=int(input('enter an odd number 3-11: '))

if n<3 or n>11 or n%2 !=1:
    print('Invalid input')

def magic_square(n):

    magicsquare=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicsquare.append(l)

    i=n//2
    j=n-1

    num=n*n
    count=1

    while(count<=num):
        if(i==-1 and j==n):
            j=n-2
            i=0
        else:
            if(j==n):
                j=0

            if(i<0):
                i=n-1
        
        if(magicsquare[i][j]!=0):
            j=j-2
            i=i+1
            continue

        else:
            magicsquare[i][j]=count
            count+=1
        
        i=i-1
        j=j+1

    for i in range(n):
        for j in range(n):
            print(magicsquare[i][j],end=' ')
        print()

    numbers=[]
    for k in range(1,num+1):
        numbers.append(k)
    print('\n Sum of all numbers:',sum(numbers))


    

magic_square(n)
