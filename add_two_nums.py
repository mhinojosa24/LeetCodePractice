# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def addTwoNumbers(self, l1, l2):
        return self.addTwoNumbersIterative(l1, l2)
        # return self.addTwoNumbersRecursive(l1, l2)

    def addTwoNumbersIterative(self, node1: ListNode, node2: ListNode):
        result = []
        temp = 0
        va1 = 0
        va2 = 0

        while node1 is not None or node2 is not None or temp > 0:
            if node1 is not None:
                val1 = node1.val
                node1 = node1.next

            if node2 is not None:
                val2 = node2.val
                node2 = node2.next


            num = val1 + val2 + temp
            remainder = num % 10
            temp = num // 10
            result.append(remainder)

            val1, val2 = 0, 0


        return result


    def addTwoNumbersRecursive(self, n1, n2, mod=0, result=[]):
        val1 = 0 if n1 is None else n1.val
        val2 = 0 if n2 is None else n2.val

        num_sum = val1 + val2 + mod

        if num_sum == 0:
            return result

        result.append(num_sum%10)

        n1 = None if n1 is None else n1.next
        n2 = None if n2 is None else n2.next
        return self.addTwoNumbersRecursive(n1, n2, num_sum // 10, result)

def main():
