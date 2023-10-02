import math

def find_parabola_info(A, B, C):
    # Determine the direction of the parabola
    direction = "The Graph is facing up" if A > 0 else "The Graph is facing down"
    
    # Calculate the vertex
    h = -B / (2 * A)
    k = (4 * A * C - B ** 2) / (4 * A)
    vertex = (h, k)
    
    # Determine the position of the parabola
    position = "vertical" if A != 0 else "horizontal"
    
    # Calculate the value of 'p' for the directrix
    p = abs(1 / (4 * A))
    
    # Calculate the coordinates of the focus
    focus = (h, k + p) if position == "vertical" else (h + p, k)
    
    # Determine the equation of the directrix
    if position == "vertical":
        directrix = f"y = {k - p:.2f}"
    else:
        directrix = f"x = {h - p:.2f}"
    
    # Calculate and format the quadratic formula
    if A != 0:
        discriminant = B ** 2 - 4 * A * C
        if discriminant >= 0:
            x1 = (-B + math.sqrt(discriminant)) / (2 * A)
            x2 = (-B - math.sqrt(discriminant)) / (2 * A)
            quadratic_formula = f"x = {x1:.2f} or x = {x2:.2f}"
        else:
            quadratic_formula = "No real roots"
    else:
        quadratic_formula = f"x = {(-C/B):.2f}"
    
    # Return the information
    return {
        "Quadratic Formula": quadratic_formula,
        "Direction": direction,
        "Vertex": vertex,
        "Focus": focus,
        "Directrix": directrix
    }

# Get user input for coefficients
A = float(input("Enter coefficient A: "))
B = float(input("Enter coefficient B: "))
C = float(input("Enter coefficient C: "))

# Calculate and display parabola information
parabola_info = find_parabola_info(A, B, C)
print("\nParabola Information:")
print(f'f(x)= {int(A)}x^2 + {int(B)}x + {int(C)}')
print("Direction:", parabola_info["Direction"])
print("Vertex:", parabola_info["Vertex"])
print("Focus:", parabola_info["Focus"])
print("Directrix:", parabola_info["Directrix"])
print("Quadratic Formula:", parabola_info["Quadratic Formula"])
