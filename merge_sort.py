import random

def merge_Sort(array: [int]):
    mid_point = int(len(array)/2)

    if len(array) <= 1:
        return array

    left, right = merge_Sort(array[:mid_point]), merge_Sort(array[mid_point:])

    return merge(left, right)

def merge(left: [int], right: [int]):
    
    merged_array = [] # O(1)
    left = left
    right = right

    while len(left) > 0 and len(right) > 0:
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
