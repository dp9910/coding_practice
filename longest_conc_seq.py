"""
Problem 1: Longest Consecutive Sequence (Medium) ⭐⭐⭐⭐⭐
Question: Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
Examples:
pythonExample 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive sequence is [0,1,2,3,4,5,6,7,8]. Length is 9.

Example 3:
Input: nums = []
Output: 0

Example 4:
Input: nums = [1,2,0,1]
Output: 3
Explanation: [0,1,2]
"""


nums = [100,4,200,1,3,2,4]

set_val=set(nums)

print(set_val)


max_len=0

for num in nums:
    
    if (num-1) not in set_val:

        print(num)

        current=num
       
        left=1
    print("cn",current)
    while (current+1) in set_val:
  
        current=current+1
        left=left+1
    max_len = max(max_len,left)

        


