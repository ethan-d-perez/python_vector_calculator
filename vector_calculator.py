import math

divider = "-----------------"
keywords = ["magnitude", "unit vector",
            "add", "subtract",
            "scalar", "dot product",
            "cross product", "angle between vectors",
            "projection", "rotation",
            "keywords"]

def vector_mag():
    tempText1 = "What is the rx of the vector?"
    tempText2 = "What is the ry of the vector?"
    tempText3 = "What is the rz of the vector?"

    v1 = float(input(tempText1))
    v2 = float(input(tempText2))
    v3 = float(input(tempText3))

    temp_vMag1 = math.pow(v1, 2)
    temp_vMag2 = math.pow(v2, 2)
    temp_vMag3 = math.pow(v3, 3)

    vMag = math.sqrt((temp_vMag1) + (temp_vMag2) + (temp_vMag3))
    print("Magnitude:", '{:.4e}'.format(vMag))

def vector_hat():
    tempText1 = "What is the rx of the vector?"
    tempText2 = "What is the ry of the vector?"
    tempText3 = "What is the rz of the vector?"

    v1 = float(input(tempText1))
    v2 = float(input(tempText2))
    v3 = float(input(tempText3))

    temp_vMag1 = math.pow(v1, 2)
    temp_vMag2 = math.pow(v2, 2)
    temp_vMag3 = math.pow(v3, 3)

    vMag = math.sqrt((temp_vMag1) + (temp_vMag2) + (temp_vMag3))

    if vMag != 0:
        u1 = '{:.4e}'.format(v1 / vMag)
        u2 = '{:.4e}'.format(v2 / vMag)
        u3 = '{:.4e}'.format(v3 / vMag)
    else:
        u1 = 0
        u2 = 0
        u3 = 0

    result = f'Unit Vector: <{u1}, {u2}, {u3}>'
    print(result)

def start():
    goodInput = False

    print("Keywords:", keywords)

    while goodInput == False:
        tempText1 = "What type of vector math? "
        tempText2 = "Please type in a keyword. Type keywords for a refresher. "

        tempInput = input(tempText1)
        if tempInput == "magnitude":
            print(divider)
            goodInput = True

            vector_mag()
        elif tempInput == "unit vector":
            print(divider)
            goodInput = True

            vector_hat()
        elif tempInput == "add":
            print(divider)
            goodInput = True

            #vector_add()
        elif tempInput == "sub":
            print(divider)
            goodInput = True

            #vector_sub()
        elif tempInput == "scalar":
            print(divider)
            goodInput = True

            #vector_scalar()
        elif tempInput == "keywords":
            print("Keywords:", keywords)
        else:
            print(tempText2)

start()

