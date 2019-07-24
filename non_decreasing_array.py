# class Solution:
def checkPossibility(nums):
    isChanged = False



    if len(nums) == 0 or len(nums) == 1:
        return True

    for i in range(0, len(nums) - 1):

        if nums[i] > nums[i + 1]:
            if isChanged == True:
                return False

            elif i == 0 or nums[i - 1] < nums[i + 1]:
                print('here')
                nums[i] = nums[i + 1]
                # print(nums[i])
            else:
                nums[i + 1] = nums[i]
            isChanged = True

    return True

l = [-1,4,2,3]
l2 = [4,2,3]
list = [4,2,1]
print('correct: True, result: ', checkPossibility(l))
print('correct: True, result: ', checkPossibility(l2))
print('correct: False, result: ', checkPossibility(list))
