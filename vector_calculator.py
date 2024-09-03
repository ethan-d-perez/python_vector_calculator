import math

divider = "-----------------"
keywords = ["magnitude", "unit vector",
            "add", "subtract",
            "scalar", "dot product",
            "cross product", "angle between vectors",
            "projection", "rotation",
            "keywords"]

def mag():
    tempText1 = "What is the rx of the vector? "
    tempText2 = "What is the ry of the vector? "
    tempText3 = "What is the rz of the vector? "

    v1 = float(input(tempText1))
    v2 = float(input(tempText2))
    v3 = float(input(tempText3))

    temp_vMag1 = math.pow(v1, 2)
    temp_vMag2 = math.pow(v2, 2)
    temp_vMag3 = math.pow(v3, 3)

    vMag = math.sqrt((temp_vMag1) + (temp_vMag2) + (temp_vMag3))
    print("Magnitude:", '{:.4e}'.format(vMag))

def hat():
    tempText1 = "What is the rx of the vector? "
    tempText2 = "What is the ry of the vector? "
    tempText3 = "What is the rz of the vector? "

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

def add():
    tempText1 = "What is the rx of the first vector? "
    tempText2 = "What is the ry of the first vector? "
    tempText3 = "What is the rz of the first vector? "
    tempText4 = "What is the rx of the second vector? "
    tempText5 = "What is the ry of the second vector? "
    tempText6 = "What is the rz of the second vector? "

    vx = float(input(tempText1))
    vy = float(input(tempText2))
    vz = float(input(tempText3))
    ux = float(input(tempText4))
    uy = float(input(tempText5))
    uz = float(input(tempText6))

    sumX = '{:.4e}'.format(vx + ux)
    sumY = '{:.4e}'.format(vy + uy)
    sumZ = '{:.4e}'.format(vz + uz)

    result = f'Sum: <{sumX}, {sumY}, {sumZ}'
    print(result)

def sub():
    tempText1 = "What is the rx of the first vector? "
    tempText2 = "What is the ry of the first vector? "
    tempText3 = "What is the rz of the first vector? "
    tempText4 = "What is the rx of the second vector? "
    tempText5 = "What is the ry of the second vector? "
    tempText6 = "What is the rz of the second vector? "

    vx = float(input(tempText1))
    vy = float(input(tempText2))
    vz = float(input(tempText3))
    ux = float(input(tempText4))
    uy = float(input(tempText5))
    uz = float(input(tempText6))

    sumX = '{:.4e}'.format(vx - ux)
    sumY = '{:.4e}'.format(vy - uy)
    sumZ = '{:.4e}'.format(vz - uz)

    result = f'Difference: <{sumX}, {sumY}, {sumZ}>'
    print(result)

def scalar():
    tempText1 = "What is the rx of the vector? "
    tempText2 = "What is the ry of the vector? "
    tempText3 = "What is the rz of the vector? "
    tempText4 = "What is the value of the scalar? "

    vx = float(input(tempText1))
    vy = float(input(tempText2))
    vz = float(input(tempText3))
    a = float(input(tempText4))

    productX = '{:.4e}'.format(a * vx)
    productY = '{:.4e}'.format(a * vy)
    productZ = '{:.4e}'.format(a * vz)

    result = f'Product: <{productX}, {productY}, {productZ}>'
    print(result)

def dot_product():
    tempText1 = "What is the rx of the first vector? "
    tempText2 = "What is the ry of the first vector? "
    tempText3 = "What is the rz of the first vector? "
    tempText4 = "What is the rx of the second vector? "
    tempText5 = "What is the ry of the second vector? "
    tempText6 = "What is the rz of the second vector? "

    vx = float(input(tempText1))
    vy = float(input(tempText2))
    vz = float(input(tempText3))
    ux = float(input(tempText4))
    uy = float(input(tempText5))
    uz = float(input(tempText6))

    productX = vx * ux
    productY = vy * uy
    productZ = vz * uz
    sum = '{:.4e}'.format(productX + productY + productZ)

    result = f'Dot Product: {sum}'
    print(result)

def cross_product():
    tempText1 = "What is the rx of the first vector? "
    tempText2 = "What is the ry of the first vector? "
    tempText3 = "What is the rz of the first vector? "
    tempText4 = "What is the rx of the second vector? "
    tempText5 = "What is the ry of the second vector? "
    tempText6 = "What is the rz of the second vector? "

    vx = float(input(tempText1))
    vy = float(input(tempText2))
    vz = float(input(tempText3))
    ux = float(input(tempText4))
    uy = float(input(tempText5))
    uz = float(input(tempText6))

    zx = '{:.4e}'.format((vy * uz) - (uy * vz))
    zy = '{:.4e}'.format(-1 * ((vx * uz) - (ux * vz)))
    zz = '{:.4e}'.format((vx * uy) - (ux * vy))

    result = f'Cross Product: <{zx}, {zy}, {zz}>'
    print(result)

def projection():
    tempText1 = "Assume that the second vector is being projected in respect to the first vector."
    tempText2 = "What is the rx of the first vector? "
    tempText3 = "What is the ry of the first vector? "
    tempText4 = "What is the rz of the first vector? "
    tempText5 = "What is the rx of the second vector? "
    tempText6 = "What is the ry of the second vector? "
    tempText7 = "What is the rz of the second vector? "

    print(tempText1)

    vx = float(input(tempText2))
    vy = float(input(tempText3))
    vz = float(input(tempText4))
    ux = float(input(tempText5))
    uy = float(input(tempText6))
    uz = float(input(tempText7))

    productX1 = vx * ux
    productY1 = vy * uy
    productZ1 = vz * uz
    sum1 = productX1 + productY1 + productZ1

    productX2 = vx * vx
    productY2 = vy * vy
    productZ2 = vz * vz
    sum2 = productX2 + productY2 + productZ2

    if sum2 != 0:
        a = sum1 / sum2
    else:
        a = 0

    uParallelX = a * vx
    uParallelY = a * vy
    uParallelZ = a * vz

    uPerpendicularX = ux - uParallelX
    uPerpendicularY = uy - uParallelY
    uPerpendicularZ = uz - uParallelZ

    uParallel = f'U Parallel: <{'{:.4e}'.format(uParallelX)}, {'{:.4e}'.format(uParallelY)}, {'{:.4e}'.format(uParallelZ)}>'
    uPerpendicular = f'U Perpendicular: <{'{:.4e}'.format(uPerpendicularX)}, {'{:.4e}'.format(uPerpendicularY)}, {'{:.4e}'.format(uPerpendicularZ)}>'

    print(uParallel)
    print(uPerpendicular)

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

            mag()
        elif tempInput == "unit vector":
            print(divider)
            goodInput = True

            hat()
        elif tempInput == "add":
            print(divider)
            goodInput = True

            add()
        elif tempInput == "sub":
            print(divider)
            goodInput = True

            sub()
        elif tempInput == "scalar":
            print(divider)
            goodInput = True

            scalar()
        elif tempInput == "dot product":
            print(divider)
            goodInput = True

            dot_product()
        elif tempInput == "cross product":
            print(divider)
            goodInput = True

            cross_product()
        elif tempInput == "projection":
            print(divider)
            goodInput = True

            projection()
        elif tempInput == "keywords":
            print("Keywords:", keywords)
        else:
            print(tempText2)

start()
