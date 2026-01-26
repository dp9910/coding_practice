"""
Question: Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Must do it in-place with O(1) extra space!
Examples:
pythonExample 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
  Rotate 1 step:  [7,1,2,3,4,5,6]
  Rotate 2 steps: [6,7,1,2,3,4,5]
  Rotate 3 steps: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
  Rotate 1 step:  [99,-1,-100,3]
  Rotate 2 steps: [3,99,-1,-100]

Example 3:
Input: nums = [1,2,3,4,5], k = 7
Output: [4,5,1,2,3]
"""


nums = [1,2,3,4,5,6,7]

k = 3

k_val = k%len(nums)



for _ in range(k_val):


    nums.insert(0, nums.pop()) ##rotating right to left

    #nums.append(nums.pop(0))  ##rotating left to right

print(nums)


