"""
Problem 1: Merge Intervals (Medium) ⭐⭐⭐⭐⭐
Question: Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of non-overlapping intervals.
Examples:
pythonExample 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: 
  [1,3] and [2,6] overlap → merge to [1,6]

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: 
  [1,4] and [4,5] touch at 4 → merge to [1,5]

Example 3:
Input: intervals = [[1,4],[0,4]]
Output: [[0,4]]

Example 4:
Input: intervals = [[1,4],[2,3]]
Output: [[1,4]]
Explanation:
  [2,3] is completely inside [1,4]

"""

lsts = [[1,3],[2,6],[8,10],[15,18]]

new_lst = sorted(lsts)

merged_lst = [new_lst[0]]

for j in range(1,len(new_lst)):

    current = new_lst[j]  
    print(current,merged_lst)
    if current[0] <= merged_lst[-1][1]:
       
        ##works for both case : [1,3] [2,6] and [1,7] [ 2,6]  
        #if the second list first item is less than the last item of firs list
        ##get the max for the second position which is the max of second item in first and second list
        merged_lst[-1][1] = max(merged_lst[-1][1],current[1])
    else:
        merged_lst.append(current)
print(merged_lst)


    
