



strs = "{[]}"




def match(strs):

    brck ={')':'(',
    '}':'{',
    ']':'['}


    lst=[]
    
    for i in strs:
    

        if i in brck:   ##check if i is a closing bracket,
      
            
            ##get the opening bracket and seee if its matches the list first item which should be opening bracket

        
            if brck[i] != lst[-1] or lst==[]:
                return False
            lst.pop()

        else:
            ##if its not closing bracket then, add it to the list

            lst.append(i)
    return len(lst)==0
     
print(match(strs))
