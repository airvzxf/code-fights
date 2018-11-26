def zigzag(zigzag_array):
    index = 1
    max_zigzag = 1
    actual_zigzag = 1
    last_number = zigzag_array[0]
    should_be_bigger = None

    while index < len(zigzag_array):
        actual_number = zigzag_array[index]

        if actual_number > last_number and should_be_bigger in (False, None):
            actual_zigzag += 1
            should_be_bigger = True
        elif actual_number < last_number and should_be_bigger in (True, None):
            actual_zigzag += 1
            should_be_bigger = False
        else:
            if actual_zigzag > max_zigzag:
                max_zigzag = actual_zigzag

            if actual_number == last_number:
                actual_zigzag = 1
            else:
                actual_zigzag = 0
                index -= 2

            should_be_bigger = None

        index += 1
        last_number = actual_number

    # print("max_zigzag:", max_zigzag, zigzag_array)
    return max_zigzag


assert zigzag([9, 8, 8, 5, 3, 5, 3, 2, 8, 6]) is 4
assert zigzag([4, 4]) is 1
assert zigzag([2, 1, 4, 4, 1, 4, 4, 1, 2, 0, 1, 0, 0, 3, 1, 3, 4, 1, 3, 4]) is 6
assert zigzag([4, 2, 3, 1, 5, 3]) is 1
assert zigzag([7, 3, 5, 5, 2]) is 3
assert zigzag([3, 8, 6, 4, 5]) is 3
