list_pent=[]
sqr_pent=[]
tri_sqr_pent=[]
tri=[]
sqr=[]

for n in range(1,int(1e12)):
	if ((24*n+1)**0.5+1)%6==0:
		list_pent.append(n)
		if (n**0.5)%1==0:
			sqr_pent.append(n)
			if ((8*n+1)**0.5 -1) %2 ==0:
				tri_sqr_pent.append(n)
#	if (n**0.5)%1==0:
#			sqr.append(n)
#	if ((8*n +1)**0.5 -1) %2 ==0:
#				tri.append(n)
	if n%2e6 ==0:
		print('up to n=',n)
	n+=1

#print('# of triangle numbers:',len(tri), ',largest:',max(tri))
#print('# of square numbers:',len(sqr),',largest', max(sqr))
print('# of pentagon numbers:', len(list_pent), ',largest',max(list_pent) )
print('list of square pentagon numbers:', sqr_pent)
print('list of triangle square pentagon numbers:',tri_sqr_pent)