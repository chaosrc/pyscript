#!/usr/bin/python3

a=[1,3,5]

num=input('The number you want to caculate\n')
num=int(num)+1
dp=[x for x in range(0,num)]

def minCost():
    
    for i in range(1,num):
        tem=i
        j=0
        for j in range(0,len(a)):
            if i>=a[j]:
                dp[i]=dp[i-a[j]]+1
                #print(dp[i])
                if tem>dp[i]:
                    tem=dp[i]
            
        dp[i]=tem
        

		






if __name__ == '__main__':
    minCost()
    print(dp)