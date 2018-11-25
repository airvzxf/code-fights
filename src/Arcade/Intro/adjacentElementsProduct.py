def adjacentElementsProduct(inputArray):
    biggest_number = -1000
    array_elements = len(inputArray) - 1

    for index in range(0, array_elements):
        adjacent_multiplication = inputArray[index] * inputArray[index + 1]

        if adjacent_multiplication > biggest_number:
            biggest_number = adjacent_multiplication

    return biggest_number


assert adjacentElementsProduct([3, 6, -2, -5, 7, 3]) == 21
assert adjacentElementsProduct([-1, -2]) == 2
assert adjacentElementsProduct([5, 1, 2, 3, 1, 4]) == 6
assert adjacentElementsProduct([1, 2, 3, 0]) == 6
assert adjacentElementsProduct([9, 5, 10, 2, 24, -1, -48]) == 50
assert adjacentElementsProduct([5, 6, -4, 2, 3, 2, -23]) == 30
assert adjacentElementsProduct([4, 1, 2, 3, 1, 5]) == 6
assert adjacentElementsProduct([-23, 4, -3, 8, -12]) == -12
assert adjacentElementsProduct([1, 0, 1, 0, 1000]) == 0
