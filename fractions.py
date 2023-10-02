#get fraction input
fraction1=input('Enter your first fraction: ')
fraction2=input('Enter your second fraction: ')

#print fractions
print('fraction 1:',fraction1,' fraction 2:',fraction2)

#define numerator and denominator 1
fraction1=fraction1.split('/')
numerator1=fraction1[0]
denominator1=fraction1[1]

#define numerator and denominator 2
fraction2=fraction2.split('/')
numerator2=fraction2[0]
denominator2=fraction2[1]

#turn all variables to integers
numerator1=int(numerator1)
numerator2=int(numerator2)
denominator1=int(denominator1)
denominator2=int(denominator2)

#get decimal numerator1 / denominator1
fraction1=int(numerator1)/int(denominator1)

#find numerator of the division of fractions
divisionnumerator=int(numerator1)*int(denominator2)

#find denominator division of 2 fractions
divisiondenominator=denominator1*int(numerator2)

#find numerator of 2 fractions multiplied
multiplynumerator=int(numerator1)*int(numerator2)

#additionnumerator
additionnumerator=(numerator1*denominator2)+(numerator2*denominator1)

#denominator 2 fractions multiplied
multiplydenominator=denominator1*denominator2

#numerator fraction1-fraction2
subtractnumerator=(numerator1*denominator2)-(numerator2*denominator1)

#remain of first fraction
mixnum=numerator1%denominator1

#divide first fraction for a decimal
mixwhole=numerator1/denominator1

#print sum difference product and quotient of the 2 fractions
print('Addition of fraction:',additionnumerator/multiplydenominator,'\n')
print('Subtraction of fractions:',subtractnumerator/multiplydenominator,'\n')
print('Multiplication of fractions:',multiplynumerator/multiplydenominator,'\n')
print('Division of fractions:',divisionnumerator/divisiondenominator,'\n')

#discover improper fraction or not for first fraction
if numerator1>denominator1:
    print('Fraction 1 is an improper fraction')
    if mixnum==0:
        print('Fraction 1 as a mixed number:',mixwhole)
    else:
        print('Fraction 1 as a mixed number:',mixwhole,mixnum,denominator1)
else:
    print('fraction 1 is not an improper fraction')

#fraction 1 as a decimal
print('Decimal approximation of a fraction 1:',fraction1%.2,'\n')

#ask for a grade as an integer between 0-4:
grade=int(input('Enter in a GPA for the class 0-4 integer: '))

#print letter grade that corresponds
if grade==4:
    print('You got an A!')
elif grade==3:
    print("You got a B!")
elif grade==2:
    print("You got a C!")
elif grade==1:
    print("You got a D!")
elif grade==0:
    print("You got a F!")
else:
    print('That is not a grade')
