"""
You must implement the nextGreaterElement() function.

For each element i in a list, it finds the first element to its right which is greater than i.

For any element that such a value does not exist, the answer is -1.

Example 1:
  input:
 
    [10, 6, 3, 2, 8, 1]
    
  output:
  
    [-1, 8, 8, 8, -1, -1]


"""
def nextGreaterElement(arr):
    if not arr:
        return arr
    
    
    result = [-1] * len(arr)

    for index, current_element in enumerate(arr):
        
        for j in range(index + 1, len(arr)):
            
            if current_element < arr[j]:
                result[index] = arr[j]
                break
                 

    return result



arr = [10, 6, 3, 2, 8, 1]
print(nextGreaterElement(arr)) # [-1, 8, 8, 8, -1, -1]
            
            
    https://realpython.com
        
        
        
hand holding through the obvious


Good:
 - restated the prompt.
 - asking clarifying questions
 - good questions
 - working through the problem
 - catches his own errors

Bad:
 - get engineering jargon
 - got stuck for too long
 - does not know python well?
 - did not want to get help from the interviewer, continued to push forward with their own idea.
 - continues to write his own idea... stubborn not team player
 - gets runtime/ space complexity but needs more work.
 

