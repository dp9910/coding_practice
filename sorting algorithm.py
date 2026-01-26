"sorting algorithm"


nums = [-1,0,1,2,-1,-4]


left=0
right=len(nums)-1

while left<right:

    for j in range(left,len(nums)):

        if nums[left] > nums[j]:

            nums[left],nums[j] =nums[j],nums[left]

    print(nums)
    left=left+1

print(nums)
        