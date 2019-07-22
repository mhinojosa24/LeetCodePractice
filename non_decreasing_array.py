class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        isDecending = True
        l = [1, 2, 3, 4, 5, 6, 7]

        if len(nums) == 0 or len(nums) == 1:
            return True

        for i in range(0, len(nums)):
            if 1 <= nums[i] < len(nums):
                print('True')
#                 if i == len(nums):
#                     return True

                # continue

            isDecending = False
