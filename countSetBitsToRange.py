class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        # return the count
        count=0
        for i in range(1,n+1):
            while i!=0:
                if i&1==1:
                    count=count+1
                i=i>>1
            count=count+i
        return count


# basic version
# def countSetBits(n):
#     count=0
#     while n!=0:
#         if n&1==1:
#             count=count+1
#         n=n>>1
#     return count

# print(countSetBits(5))
