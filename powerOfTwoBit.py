def powerOfTwoBit(n):
    if n==0:  #edge case
        return False 
    flag=0
    while n!=0: 
        if n&1==1 and flag==0:
            flag=1
            flag=flag+1
        elif n&1==1 and flag>0:
            return False
        n=n>>1
    return True
print(powerOfTwoBit(4))
    
