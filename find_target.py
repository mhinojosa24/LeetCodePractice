'''
    Given a sorted array of numbers and a target value, find the duplicate count of target number.
'''

def binary_search(array, target, is_left):
    start_index = 0
    end_index = len(array)
    result = None

    while start_index <= end_index:
        middle = (start_index + end_index) // 2
        # print(middle)
        if target == array[middle]:
            result = middle

            if is_left:
                end_index = middle
                middle = (start_index + end_index) // 2

            else:
                start_index = middle
                middle = (start_index + end_index) // 2

        if target > array[middle]:
            start_index = middle
            middle = (start_index + end_index) // 2

        if target < array[middle]:
            end_index = middle
            middle = (start_index + end_index) // 2

    return result


def main():
    arry = [1, 2, 2, 2, 2, 3, 5, 7, 12, 20]
    target = 2
    left = True
    result = binary_search(arry, target, left)

    print(result)




if __name__ == '__main__':
    main()
