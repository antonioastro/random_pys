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
		return 0 #this means the number is not divisible into b^p
	elif n/x>1 and (n/x)%b!=0: 
		return int(math.floor(n/x)) #this means the number divides in, but there is a remainder that isn't a multiple of b
	else:
		return True #carrys for all others

list=[]

while p>-5: #only continue for up to 5 sexagesimal places
	if p==-1:
		list.append(';') #separates integer and fractional parts
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
        list.pop() #remove trailing zeros
    if list[len(list)-1]==';': #remove the separator if there are no sexagesimal places (i.e they are all 0)
        list.pop()
    i+=1

print(list)