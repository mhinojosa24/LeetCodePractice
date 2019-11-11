def addToarrayForm(a: [int], k: int):

    a[-1] += k
    for i in range(len(a) - 1, -1, -1):
        carry, a[i] = divmod(a[i], 10)
        if i:
            a[i-1] += carry
    if carry:
        a = list(map(int, str(carry))) + a
    return a


if __name__ == "__main__":
    a, k = [1,2,0,0], 34
    # print(addToarrayForm(a, k))
    print('RESULT: {}, expected => {}\n'.format(addToarrayForm(a, k), [1,2,3,4]))
    a, k = [2,7,4], 181
    print('RESULT: {}, expected => {}\n'.format(addToarrayForm(a, k), [4,5,5]))
    a, k = [2,1,5], 806
    print('RESULT: {}, expected => {}\n'.format(addToarrayForm(a, k), [1,0,2,1]))
    a, k = [9,9,9,9,9,9,9,9,9,9], 1
    print('RESULT: {}, expected => {}\n'.format(addToarrayForm(a, k), [1,0,0,0,0,0,0,0,0,0,0]))
