

'''
561. Array Partition I

Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
'''

def arrayPairSum(nums: [int]) -> int:
        max_sum = 0
        looping = True
        i = 0
        nums.sort()

        while looping:
            if i >= len(nums):
                looping = False
            else:
                if nums[i] > nums[i+1]:
                    max_sum += nums[i+1]
                else:
                    max_sum += nums[i]
                i += 2

        return max_sum

if __name__ == '__main__':
    num = [1,4,3,2, 6, 7, 8, 9]
    print(arrayPairSum(num))
