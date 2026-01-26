"""
## Problem 2: Container With Most Water (Medium) ⭐⭐⭐⭐⭐

**Question:** You are given an array `height` where each element represents the height of a vertical line. Find two lines that together with the x-axis form a container that holds the most water.

**Return the maximum area of water the container can store.**

### **Visual:**
```
height = [1,8,6,2,5,4,8,3,7]

     |               |
     |       |       |       |
     |       |   |   |   |   |
     |   |   |   |   |   |   |
 |   |   |   |   |   |   |   |
 1   8   6   2   5   4   8   3   7
 0   1   2   3   4   5   6   7   8

Area = min(height[left], height[right]) × (right - left)

Best: lines at index 1 and 8
Area = min(8, 7) × (8 - 1) = 7 × 7 = 49
"""

left=0

height=[1,8,6,2,5,4,8,3,7]

max_area=0
for j in range(len(height)):

    for k in range(j,len(height)):


        area = min(height[k],height[j])*(k-j)

        if area >= max_area:

            max_area=area
print(max_area)





left=0
right=len(height)-1
max_area=0

while left<right:

    area = min(height[left],height[right])*(right-left)

    max_area = max(max_area,area)

    if height[left] < height[right]:

        left=left+1
    else:
        right=right-1
print(max_area)




