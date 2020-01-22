
'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
'''



def isOverFlowed(x: int):
        if ((-2 ** 31) <= x <= (2 ** 31)):
            return False
        else:
            return True

def reverse(x: int):
    if x < 0:
        x = int(str(abs(x))[::-1]) * -1
    else:
        x = int(str(x)[::-1])

    if isOverFlowed(x):
        return 0
    else:
        return x

if __name__ == '__main__':
    x = -2147483648

    print(reverse(x))
