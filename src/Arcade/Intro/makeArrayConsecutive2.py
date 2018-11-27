def makeArrayConsecutive2(statues):
    statues.sort()
    min_number = statues[0]
    max_number = statues[-1]
    total_statues = len(statues) - 1

    ratiorg = max_number - min_number - total_statues

    print("ratiorg: ", ratiorg, "statues: ", statues)

    return ratiorg


assert makeArrayConsecutive2([6, 2, 3, 8]) is 3
assert makeArrayConsecutive2([0, 3]) is 2
assert makeArrayConsecutive2([5, 4, 6]) is 0
assert makeArrayConsecutive2([6, 3]) is 2
assert makeArrayConsecutive2([1]) is 0
