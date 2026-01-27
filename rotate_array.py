
"""
Problem 1: Find Minimum in Rotated Sorted Array (Medium) ⭐⭐⭐⭐⭐
Question: Suppose an array of length n sorted in ascending order is rotated between 1 and n times. Given the rotated array nums, return the minimum element.
You must write an algorithm that runs in O(log n) time.
Examples:
pythonExample 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] rotated 0 times (not rotated).

Example 4:
Input: nums = [2,1]
Output: 1

Example 5:
Input: nums = [1]
Output: 1
```
"""
nums = [11,13,15]


def rotate(nums):

    left=0

    right=len(nums)-1


    if len(nums)==1:
        return nums[0]
    
    while left!=right:

        if  nums[right] > nums[right-1]:

            right=right-1

        else:
            return nums[right]

    return nums[right]



nums = [4,5,6,7,8,9,1]


#binary search
##get the mid

### since its sorted until its not
#going from left to right, regular sorted array, mid has a lower value than right
##if mid > right, then the minium value has to be on the right side of mid
##so left becomes mid+1
##but if mid < right, then we know that the value has to be on the left side including the mid value


####binary search

def rotate(nums):

    left=0
    right=len(nums)-1

    if len(nums)==1:
        return nums[0]

    while left<right:

        mid = (left+right)//2

        print(nums[mid],nums[right],nums[left])
        if nums[mid] > nums[right]:

            left=mid+1
        else:
            right=mid
    return nums[left]



print(rotate(nums))


