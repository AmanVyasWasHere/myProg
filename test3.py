import sys
ser=[]
primelist=[]
def prime(x):

    if x>1:
        for y in range(2,x):
            if x%y==0:
                break
        else:
            primelist.append(x)
            
def fib(n):
    a, b= 1, 1
    for i in range(n-1):
        a, b= b, a+b
    return a
for c in range(100):
    prime(c)
# print(primelist)
    

g=1  
l=0      
for i in range(20):
    if i%2==0:
        ser.append(fib(g))
        g+=1
    else :
        ser.append(primelist[l])
        l+=1
# print(ser)
arg=sys.argv
print(ser[int(arg[1])-1])


    

    
