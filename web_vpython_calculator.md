Web VPython version of the calculator. This code was still written by me but utilizes their library.
The website can be found at glowscript.org
```
Web VPython 3.2

divider = "------------------------"
keywords = ["magnitude", "unit vector",
            "add", "subtract",
            "scalar", "dot product",
            "cross product", "angle between vectors",
            "projection", "rotation",
            "keywords"]
    
def start():
    goodInput = False
    
    print("Keywords:", keywords)
    
    while goodInput == False:
        tempText1 = "What type of vector math?"
        tempText2 = "Please type in a keyword. Type keywords for a refresher."
        
        tempInput = input(tempText1)
        if tempInput == "magnitude":
            print(divider)
            goodInput = True
            
            vector_mag()
        elif tempInput == "unit vector":
            print(divider)
            goodInput = True
            
            unit_vector()
        elif tempInput == "add":
            print(divider)
            goodInput = True
            
            vector_add()
        elif tempInput == "sub":
            print(divider)
            goodInput = True
            
            vector_sub()
        elif tempInput == "scalar":
            print(divider)
            goodInput = True
            
            vector_scalar()
        elif tempInput == "keywords":
            print("Keywords:", keywords)
        else:
            print(tempText2)

def vector_mag():
    tempText1 = "What is the rx of the vector?"
    tempText2 = "What is the ry of the vector?"
    tempText3 = "What is the rz of the vector?"
    
    v = vec(0, 0, 0)
    
    v.x = input(tempText1)
    v.y = input(tempText2)
    v.z = input(tempText3)
    
    result = mag(v)
    print("Magnitude:", result)

def unit_vector():
    tempText1 = "What is the rx of the vector?"
    tempText2 = "What is the ry of the vector?"
    tempText3 = "What is the rz of the vector?"
    
    v = vec(0, 0, 0)
    
    v.x = input(tempText1)
    v.y = input(tempText2)
    v.z = input(tempText3)
    
    result = hat(v)
    print("Unit Vector:", result)
    
def vector_add():
    tempText1 = "What is the rx of the first vector?"
    tempText2 = "What is the ry of the first vector?"
    tempText3 = "What is the rz of the first vector?"
    tempText4 = "What is the rx of the second vector?"
    tempText5 = "What is the ry of the second vector?"
    tempText6 = "What is the rz of the second vector?"
    
    v = vec(0, 0, 0)
    u = vec(0, 0, 0)
    
    v.x = float(input(tempText1))
    v.y = float(input(tempText2))
    v.z = float(input(tempText3))
    u.x = float(input(tempText4))
    u.y = float(input(tempText5))
    u.z = float(input(tempText6))
    
    result = v + u
    print("Sum:", result)
    
def vector_sub():
    tempText1 = "What is the rx of the first vector?"
    tempText2 = "What is the ry of the first vector?"
    tempText3 = "What is the rz of the first vector?"
    tempText4 = "What is the rx of the second vector?"
    tempText5 = "What is the ry of the second vector?"
    tempText6 = "What is the rz of the second vector?"
    
    v = vec(0, 0, 0)
    u = vec(0, 0, 0)
    
    v.x = input(tempText1)
    v.y = input(tempText2)
    v.z = input(tempText3)
    u.x = input(tempText4)
    u.y = input(tempText5)
    u.z = input(tempText6)
    
    result = v - u
    print("Difference:", result)
    
def vector_scalar():
    tempText1 = "What is the scalar (for fractions type a decimal)?"
    tempText2 = "What is the rx of the vector?"
    tempText3 = "What is the ry of the vector?"
    tempText4 = "What is the rz of the vector?"
    
    a = float(input(tempText1))
    v = vec(0, 0, 0)
    
    v.x = input(tempText2)
    v.y = input(tempText3)
    v.z = input(tempText4)
    
    result = a * v
    print("Scalar * v:", result)

start()
```
