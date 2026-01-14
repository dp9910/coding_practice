'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


strs =["flower","flow","flight"]

strs=["ab","a"]

def find_longest(strs):


    i = strs[0]
    result=''
    pos=0

    for char in i:

        for j in range(1,len(strs)):

            str_cs = strs[j]
            print(str_cs)
            print(pos,len(str_cs))
            if pos >(len(str_cs)-1) or char !=str_cs[pos]:
                return result
        pos=pos+1
        result=result + char


print(find_longest(strs))