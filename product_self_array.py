"""
Problem 3: Product of Array Except Self (Medium) ⭐⭐⭐⭐⭐
Question: Given an integer array nums, return an array answer where answer[i] is the product of all elements except nums[i].
Constraints:

Must run in O(n) time
Cannot use division
Can you do it with O(1) extra space? (output array doesn't count)

Examples:
pythonExample 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation:
  answer[0] = 2 × 3 × 4 = 24
  answer[1] = 1 × 3 × 4 = 12
  answer[2] = 1 × 2 × 4 = 8
  answer[3] = 1 × 2 × 3 = 6

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
Explanation:
  answer[0] = 1 × 0 × (-3) × 3 = 0
  answer[1] = (-1) × 0 × (-3) × 3 = 0
  answer[2] = (-1) × 1 × (-3) × 3 = 9
  answer[3] = (-1) × 1 × 0 × 3 = 0
  answer[4] = (-1) × 1 × 0 × (-3) = 0
  """

s=[-1,1,0,-3,3]


left=0
right=0

cj=[]

while right<len(s):

    ts=s
    ts[left],ts[right]=ts[right],ts[left]
    print(ts)

    ml=1
    right=right+1
    for i in range(1,len(s)):

        ml = ts[i]*ml
    cj.append(ml)
print(cj)

