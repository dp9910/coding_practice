'''
**Question:** Given a sorted array, find the index of `target`. Return -1 if not found.
```
Input: arr = [1, 3, 5, 7, 9], target = 7

'''


arr=[1,3,5,7,9]
target=7

def val(arr,target):

    left=0
    right=len(arr)-1


    while left<=right:

        mid = (left+right)//2

       

        if arr[mid] ==target:
            return mid


        ####if the target value is greater than midd value, meaning the target value has to be on the
        ## right side of mid array, so anything before mid can be ignored.
        ## same if target value less than mid, the right side after mid value can be ignored 
        ## move the pointer to the mid for the right side. so now the search is between left and mid point

        if arr[mid] < target:

            left=mid+1
        else:

            right=mid-1
    return -1


print(val(arr,target))




      