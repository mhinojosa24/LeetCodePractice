# class Solution:
def checkPossibility(nums):
    isDecending = True



    if len(nums) == 0 or len(nums) == 1:
        return True

    for i in range(0, len(nums)):
        # print(i + 1)
        if (i + 1 > len(nums) - 1) == False:
            # print('hi')
            if nums[i] >= nums[i + 1]:
                next_num = nums[i + 1]
                new_num = ((nums[i] - next_num) - 1)

                if new_num == 0:
                    new_num = 1

                if (new_num < next_num) == False:
                    print('here')
                    nums[i + 1] = nums[i] + next_num
                    print(nums[i + 1])

                # print(isDecending)
                if 1 <= new_num < next_num and isDecending == True:
                    print('here')
                    isDecending = False
                    print(isDecending)

                return False
    else:
        if isDecending == True:
            return True

list = [4,2,1]
print(checkPossibility(list))
