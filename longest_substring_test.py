"""
Problem 2: Longest Substring Without Repeating Characters (Medium) ⭐⭐⭐⭐⭐
Question: Given a string s, find the length of the longest substring without repeating characters.
Examples:
pythonExample 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with length 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with length 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with length 3.
Notice that "pwke" is a subsequence, not substring.

Example 4:
Input: s = ""
Output: 0

Example 5:
Input: s = "abcdefg"
Output: 7
"""



s = "bbbb"
left=0

len_set=[]

right=len(s)
chars=""

for st in range(len(s)-1):

    chars=s[st]
    left=1+st

    seen=set()

    seen.add(chars)
    
   
    while left<right:

      

        if s[left] not in seen:
            
            seen.add(s[left])
          
            left=left+1
        else:
            
            break
    len_set.append(len(seen))
    if left==len(s):
        break

print(max(len_set))

def find_max_str(s):

    left=0
    max_len=0

    seen=set()

    for right in range(len(s)):


        while s[right] in seen:

            seen.remove(s[left])
            left=left+1
        seen.add(s[right])

        max_len = max(max_len,len(seen))
    return max_len


    
