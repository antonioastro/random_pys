import math

print('input number')
n=float(input())
m=n

print('input base')
b=float(input())

p=100
e=20

def div60(b,n,p):
	x=b**p
	if (n/x)<1:
		return 0
	elif n/x>1 and (n/x)%b!=0:
		return int(math.floor(n/x)) 
	else:
		return True 	

list=[]

while p>-s-1:
	if p==-1:
		list.append(';')
	x=b**p
	if div60(b,n,p)==0:
		if len(list)!=0:
			list.append(div60(b,n,p))
		p+=-1
	elif div60(b,n,p) == True:
		list.append(int(n/x))
		n=x*((n/x)-int(math.floor(n/x)))
		p+=-1
	else:
		list.append(div60(b,n,p))
		n=x*((n/x)-(n//x))
		p+=-1

i=0
while i<len(list):
    if list[len(list)-1]==0:
        list.pop()
    if list[len(list)-1]==';':
        list.pop()
    i+=1

print(list)