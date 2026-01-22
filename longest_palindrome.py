"""

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""


def long_pal(str):

    start=0
    max_len=0

    if str=="":
        return ""



    def expand_center(left,right):

        while left>=0 and right <len(str) and str[left]==str[right]:
        
            left=left-1
            right=right+1

        return right - left -1

    
    for j in range(len(str)):

   
        len1=expand_center(j,j)

        len2 = expand_center(j,j+1)

        current_len = max(len1,len2)

        if current_len > max_len:

            max_len = current_len
            start = j - (current_len - 1) // 2
    
    return str[start:start+max_len]


str='bbb'
print(long_pal(str))
