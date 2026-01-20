
'''
Question: Write a function that reverses a string in-place. The input string is given as an array of characters.
Must solve in O(1) extra space!
Examples:
pythonExample 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

'''


s = ["h","e","l","l","o"]


def rev_str(s):

    left=0
    right=len(s)-1

    while left<right:

        s[left],s[right] = s[right],s[left]

        left=left+1
        right=right-1
    return s
print(rev_str(s))




'''


Problem 2: Valid Palindrome (Easy) ⭐⭐⭐⭐⭐
Question: A string is a palindrome if it reads the same forward and backward. Ignore non-alphanumeric characters and case.
Examples:
pythonExample 1:
Input: s = "A man, a plan, a canal: Panama"
Output: True
Explanation: "amanaplanacanalpanama" is a palindrome

Example 2:
Input: s = "race a car"
Output: False
Explanation: "raceacar" is not a palindrome

Example 3:
Input: s = " "
Output: True
Explanation: Empty string is considered palindrome

'''

s= "A man, a plan, a canal: Panama"
s='ra c ac'
print(len(s))

def val_pal(s):

    left=0
    right=len(s)-1

    while left<right and not s[left].isalpha():
        left=left+1
    while left<right and not s[right].isalpha():
        right=right-1
 


    if s[left].lower() != s[right].lower():
        return False
    return True
print(val_pal(s))




'''

Problem 3: First Unique Character (Easy) ⭐⭐⭐⭐
Question: Given a string, find the first non-repeating character and return its index. If it doesn't exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
Explanation: 'l' appears only once and is first

Example 2:
Input: s = "loveleetcode"
Output: 2
Explanation: 'l' and 'o' repeat, 'v' is first unique

Example 3:
Input: s = "aabb"
Output: -1
Explanation: All characters repeat

'''
s='aabb'

def repeat(s):

    
    i=0
    while i < len(s):
  
        if s[i] not in s[i+1:]:
            return i
        else:
            i=i+2
    
    return -1

print(repeat(s))


'''
Question: Given a string, reverse the order of words. A word is a sequence of non-space characters. Multiple spaces should become a single space.
Examples:
pythonExample 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Trim leading/trailing spaces

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: Multiple spaces become one

'''

s = "  hello world  "


right= len(s)-1
left=0
strs=""

lst=[]
char=""

while left <len(s):
    char=""
    while left <len(s) and s[left]!= " " :
        char=char+s[left]
        left=left+1
    lst.append(char)
    if left < len(s) and s[left] == " " :
        left=left+1

left=0
right=len(lst)-1
new_lst=lst

while left<right:

    new_lst[left],new_lst[right] = new_lst[right],new_lst[left]
    left=left+1
    right=right-1
print(new_lst)

char=""
for j in range(len(new_lst)):

    if new_lst[j] != "":
        for chars in new_lst[j]:
            char=char+chars
        char = char + ' '
