"""
## Problem 2: Search in Rotated Sorted Array (Medium) ⭐⭐⭐⭐⭐

**Question:** Given the rotated sorted array `nums` (with **distinct** values) and an integer `target`, return the **index** of `target` if it is in `nums`, or `-1` if it is not.

**You must write an algorithm with O(log n) runtime complexity.**

### **Examples:**
````python
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Example 4:
Input: nums = [4,5,6,7,0,1,2], target = 5
Output: 1

"""


nums=[1]
target=3


def rotate(nums,target):

    left=0
    right=len(nums)-1



    while left<right:

        mid = (left+right)//2


        if nums[mid]==target:
            return mid
            
        if nums[mid] >= target and nums[left] <= target:

            right=mid
        else:
            left=mid+1
         
    
    if nums[left]!=target:
        return -1
    return left
print(rotate(nums,target))




