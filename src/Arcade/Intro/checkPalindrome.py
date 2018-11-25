def checkPalindrome(inputString):
    half_word_size = int(len(inputString) / 2)

    for index in range(0, half_word_size):
        last_index = - (1 + index)
        if inputString[index] != inputString[last_index]:
            return False

    return True


assert checkPalindrome("aabaa") is True
assert checkPalindrome("abac") is False
assert checkPalindrome("a") is True
assert checkPalindrome("az") is False
assert checkPalindrome("z") is True
assert checkPalindrome("aaabaaaa") is False
assert checkPalindrome("zzzazzazz") is False
assert checkPalindrome("hlbeeykoqqqqokyeeblh") is True
assert checkPalindrome("hlbeeykoqqqokyeeblh") is True
assert checkPalindrome("zz") is True
