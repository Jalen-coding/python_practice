#get points for calculation
point1=input('enter first point as x,y: ')
point2=input('enter second point as x,y: ')
point3=input('enter third point as x,y: ')

point1=point1.split(',')
point2=point2.split(',')
point3=point3.split(',')

x1=int(point1[0])
y1=int(point1[1])

x2=int(point2[0])
y2=int(point2[1])

x3=int(point3[0])
y3=int(point3[1])

print(f'\npoint 1: {int(x1),int(y1)} point 2: {int(x2),int(y2)} point 3: {int(x3),int(y3)}\n')

print(f'Starting Triangle: {x1,y1}, {x2,y2}, {x3,y3}\n')

#rotate the triangle
def rotate():
    y1=int(point1[0])
    x1=int(point1[1])*-1

    y2=int(point2[0])
    x2=int(point2[1])*-1

    y3=int(point3[0])
    x3=int(point3[1])*-1
    
    print(f'\nRotated triangle: {x1,y1}, {x2,y2}, {x3,y3}\n')

#reflect triangle
def reflect():
    axis=input("Type 'x' to reflect over x-axis and 'y' to reflect over y-axis: ")

    reflected=''

    if axis=='x':
        x1=int(point1[0])*-1
        x2=int(point2[0])*-1
        x3=int(point3[0])*-1
        y1=int(point1[1])
        y2=int(point2[1])
        y3=int(point3[1])
        reflected=print(f'\nReflected Triangle: {x1,y1}, {x2,y2}, {x3,y3}')

    elif axis=='y':
        y1=int(point1[1])*-1
        y2=int(point2[1])*-1
        y3=int(point3[1])*-1
        x1=int(point1[0])
        x2=int(point2[0])
        x3=int(point3[0])
        reflected=print(f'\nReflected Triangle: {x1,y1}, {x2,y2}, {x3,y3}')

    else:
        print('Invalid axis')
    
    return reflected

#Translate Triangle
def translate():
    dx=int(input('How much would you like to x translate by: '))
    dy=int(input('How much would you like to y translate by: '))

    x1=int(point1[0])+dx
    y1=int(point1[1])+dy

    x2=int(point2[0])+dx
    y2=int(point2[1])+dy

    x3=int(point3[0])+dx
    y3=int(point3[1])+dy

    translated=print(f'\nTranslated Triangle: {x1,y1}, {x2,y2}, {x3,y3}')

    return translated

translate()
reflect()
rotate()
