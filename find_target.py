'''
    Given a sorted array of numbers and a target value, find the duplicate count of target number.
'''

def binary_search(array, target, is_left):
    start_index = 0
    end_index = len(array) - 1
    result = -1

    if len(array) == 0:
        return result

    if array[start_index] and array[end_index] == target:
        return len(array)


    while start_index <= end_index:
        middle = (start_index + end_index) // 2

        if target == array[middle]:
            result = middle

            if is_left:
                end_index = middle - 1
            else:
                start_index = middle + 1


        if target > array[middle]:
            start_index = middle + 1


        if target < array[middle]:
            print('value: ', array[middle])
            end_index = middle - 1

    return result



def get_result(array, target):
    first_duplicate = binary_search(array, target, True)
    last_duplicate = binary_search(array, target, False)
    msg = 'Oops it seems that array is empty'
    msg2 = 'Oops it seems like we did not find target value'
    print('first index found: ', first_duplicate)
    print('last index found: ', last_duplicate)
    if first_duplicate < 0:
        return msg2
    else:
        result = (last_duplicate - first_duplicate) + 1
        return result

def main():
    target = 2
    array = [1, 2, 2, 2, 2, 2, 2, 2, 2, 5, 7]
    result = get_result(array, target)

    print(result)




if __name__ == '__main__':
    main()
