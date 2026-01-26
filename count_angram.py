



def freq_count(word):
    count={}
    for fruit in word:

        count[fruit] = count.get(fruit,0)+1
    return count

strs = ["eat","tea","tan","ate","nat","bat"]
strs=["a"]
strs=[[""]]

val=[]

for j in range(len(strs)):

    ct= freq_count(strs[j])


    for k in range(j+1,len(strs)):

        pt = freq_count(strs[k])

        if ct==pt:
            val.append(strs[j])
            val.append(strs[k])
           

for i in strs:
    if i not in val:
        print(i)

"""
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
  "eat", "tea", "ate" are anagrams of each other
  "tan", "nat" are anagrams of each other
  "bat" is alone

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""


strs = ["eat","tea","tan","ate","nat","bat"]



    
