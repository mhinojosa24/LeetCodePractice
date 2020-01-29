import random


'''

- Merge Sort is useful for sorting linked lists.
- Merge Sort is a stable sort which means that the same element in an array maintain their
original positions with respect to each other.
- Overall time complexity of Merge sort is O(nLogn). It is more efficient as it is in
worst case also the runtime is O(nlogn)
- The space complexity of Merge sort is O(n). This means that this algorithm takes a
lot of space and may slower down operations for the last data sets.
'''


def merge_Sort(array: [int]):
    mid_point = int(len(array)/2)

    if len(array) <= 1:
        return array

    left, right = merge_Sort(array[:mid_point]), merge_Sort(array[mid_point:])

    return merge(left, right) #O(n log(n))

def merge(left: [int], right: [int]):

    merged_array = [] # O(1)
    left = left
    right = right

    # as long as the length of both arrays are not less than 0
    while len(left) > 0 and len(right) > 0: #O(n+m) => O(n)
        if left[0] < right[0]:
            merged_array.append(left.pop(0))
        else:
            merged_array.append(right.pop(0))

    # if one of the arrays still have elements => extend the returning array
    return merged_array + left + right

if __name__ == '__main__':
    numbers = []
    for _ in range(0, 20):
        number = random.randrange(0, 100)
        numbers.append(number)

    print(merge_Sort(numbers))
