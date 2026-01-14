'''
Question: You have two sorted linked lists. Merge them into one sorted list.
'''

list1=[1,2,3]

list2=[1,3,4]


class ListNode:

    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def mergelist(list1,list2):


    dummy = ListNode(0)
    current=dummy

    while list1 and list2:

        if list1.val < list2.val:   ##if list1 has smaller value than list 2

            current.next= list1.val  ##attach list1 node
            list1 = list1.next      ##move list1 forward
        else:

            current.next=list2.val   ##attach list 2 node
            list2= list2.next     ##move list2 forward
        
        current = current.next  ###move current forward
    
    if list1:
        current.next=list1
    else:
        current.next=list2
    return dummy.next

        
print(mergelist(list1,list2))  

    


