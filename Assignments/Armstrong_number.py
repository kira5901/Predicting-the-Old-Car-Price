#def order(n):
#    x=0
#    while(n!=0):
#        x+=1
#        n=n//10
#    return x
#
#def armstrong(n):
#    num=n
#    x=order(n)
#    s=0
#    while(n!=0):
#        d=n%10
#        s+=d**x
#        n=n//10
#    if num==s:
#        print("It is Armstrong number")
#    else:
#        print("Not Armstrong number")
#armstrong(int(input("Enter number of your choice")))

import numpy as np
a=np.array([[1,2,3],[0,1,4]])
print(a.ndim)