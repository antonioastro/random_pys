def div6(n):
	ans = n*n*n +3*n*n +2*n
	if ans % 6 == 0:
		return True
	else:
		return False
		
n=1
max_n=1e9
count=0
list=[]
while n<max_n:
	if div6(n)==True:
		count+=1
	else: 
		list.append(n)
	n+=1
if count==max_n-1:
	print('True for all', 1,'< x <',int(max_n))
else:
	print('Does not hold for x=',list)