def isbadversion(bad,val):
    if val>=bad:
        return 'bad'
    else:
        return 'not bad'

def findfirstbad(n,bad):
    left=1
    right=n
    while left<right:
        mid = (left+right)//2

        if isbadversion(bad,mid)== 'bad':
            #if the mid point is bad, then we know everything on the right is already bad so there 
            #is no point looking further right as we need to find the first bad one
            # so we move the right pointer to midpoint
            #use mid not mid-1 as the mid itself could be the first bad version

            right=mid

        else:

            ##but if the midpoint is not bad, then we know the bad version hasn't started yet
            ###so we need to move the left pointer mid and start looking from there
            ## we can skip mid as we know it is still good

            left=mid+1

    return right


        

        
        

        




