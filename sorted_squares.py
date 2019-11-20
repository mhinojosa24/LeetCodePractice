
'''

Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number, also in sorted non-decreasing order.

'''



class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        newlist = []

        for i in range(len(A)):

            num = A[i] * A[i]
            newlist.append(num)

        newlist.sort()
        return newlist
