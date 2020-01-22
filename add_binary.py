'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

def add_binary(a: str, b: str):

    max_len = max(len(a), len(b))
    int_a = int(a)
    int_b = int(b)
    res = ''
    carry = 0

    for _ in range(0, max_len):

        # get the last digit and update the current integer
        num1 = int_a % 10
        int_a = int_a // 10
        num2 = int_b % 10
        int_b = int_b // 10

        # get the sum for the resulting number
        res_num = (num1 + num2 + carry) % 2

        # if greater than 2; get the sum to carry
        carry = (num1 + num2 + carry) // 2

        # convert number to string and concatenate to the result
        res = str(res_num) + res

    #  check if there is a number to carry else return the result
    if carry > 0:
        return '1' + res
    else:
        return res


if __name__ == '__main__':
    a = '1010'
    b = '1011'
    print(add_binary(a, b))
