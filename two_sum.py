"""
Question: Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that i ≠ j ≠ k and nums[i] + nums[j] + nums[k] = 0.
The solution set must not contain duplicate triplets.
Examples:
pythonExample 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
  -1 + 0 + 1 = 0
  -1 + -1 + 2 = 0

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

nums = [-1, 0, 1, 2, -1, -4]

left=0
right=len(nums)-1

while left<right:

    for j in range(left,len(nums)):

        if nums[left] > nums[j]:

            nums[left],nums[j] =nums[j],nums[left]

    print(nums)
    left=left+1

sorted_arr=nums

lst=[]
seen=set()


for i in range(len(sorted_arr)):

    left=i+1
    right=len(sorted_arr)-1

    target=sorted_arr[i]




  
    while left<right:

     

        if -target > sorted_arr[left] + sorted_arr[right]:

            left=left+1

        elif -target < sorted_arr[left] + sorted_arr[right]:


            right= right-1
        else:

            in_lst=[target,sorted_arr[left],sorted_arr[right]]

            triplet_val=(target,sorted_arr[left],sorted_arr[right])
            

            if triplet_val not in seen:


                seen.add(triplet_val)  ###check if the value is in set. set offers direct lookup vs a list

                lst.append(in_lst)
          
            left=left+1
            right=right-1
    


print(lst)


        











