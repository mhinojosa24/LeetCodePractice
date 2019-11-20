

def convertToNum(numStr: str) -> int:
    result = 0

    value = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    for i in numStr:
        result = 10 * result + value[i]
    return result

def addStrings(num1: str, num2: str) -> str:
    numstr = '{}'.format((convertToNum(num1) * convertToNum(num2)))
    return numstr



if __name__ == '__main__':
    num1 = '12'
    num2 = '12'
    result = addStrings(num1, num2)
    print("result: {}, expected: {}".format(result, '144'))
