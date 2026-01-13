'''
**Question:** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with **O(log n)** runtime complexity.

### **Examples:**
```
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

'''


def search_val(n,target):

    left=0
    right=len(n)-1
    final_say=0


    while left<=right:


        mid= (left+right)//2

        print(left,right,mid,n[mid])

        if n[mid]==target:

            return mid
        
        if n[mid]<target:

            left=mid+1
        else:
            right=mid-1

    
    return left

arr=[1,3,5,6]
target=9

print(search_val(arr,target))