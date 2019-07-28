
def binaryPatternSearch(pattern, s):
    count = 0

    for i in range(0, len(s)):
        window = s[i: len(pattern) + i]
        result = isValid(window, pattern)

        if result == True:
            count += 1

    return count

def isValid(window, pattern):
    v = {'a': '0', 'e': '0', 'i': '0', 'o': '0', 'u': '0', 'y': '0'}

    for i in range(0 , len(window)):
        # print('window: ', window)
        letter = window[i]

        if len(window) != len(pattern):
            return False
        elif pattern[i] == '0':
            if letter not in v:
                return False
        elif letter in v:
            return False

    return True

p = '010'
s = 'amazing'

print('Test 1: correct: 2, result = {}'.format(binaryPatternSearch(p, s)))

p = '0'
s = 'elegant'

print('Test 2: correct: 3, result = {}'.format(binaryPatternSearch(p, s)))


p = '101'
s = 'riding'

print('Test 3: correct: 2, result = {}'.format(binaryPatternSearch(p, s)))

p = '1011'
s = 'herbivorous'

print('Test 4: correct: 1, result = {}'.format(binaryPatternSearch(p, s)))
