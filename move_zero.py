"""
Problem 1: Move Zeroes (Easy) ⭐⭐⭐⭐⭐
Question: Given an integer array, move all 0's to the end while maintaining the relative order of non-zero elements. Must do this in-place without making a copy.
Examples:
pythonExample 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Example 3:
Input: nums = [1,2,3]
Output: [1,2,3]
"""




lst=[0,1,0,3,12]
left=0


for j in range(len(lst)):

   
    if lst[j]!=0:
        lst[left]=lst[j]
        print(lst)
        left=left+1
    
for p in range(left,len(lst)):

    lst[p]=0
print(lst)
