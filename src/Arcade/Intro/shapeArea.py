def shapeArea(n):
    area = 0

    # Split the first 1/4
    for index in range(1, n):
        area += index

    # Multiply the 1/4 to 4
    area *= 4

    # Add the initial/center pixel
    area += 1

    print("Number: ", n, "area: ", area)
    return area


assert shapeArea(2) is 5
assert shapeArea(3) is 13
assert shapeArea(1) is 1
assert shapeArea(5) is 41
assert shapeArea(4) is 25
