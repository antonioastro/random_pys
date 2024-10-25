list=[]

k=1

print('input number - press enter for each place value, and x to end input')
while k>0:
    j=input()
    if j!='x':
        list.append(float(j))
    else:
        break

print('choose your base')
b=int(float(input()))

i=0
p=len(list)
for item in list:
    i+=item*b**(p-1)
    p+=-1
print(list,'_',b,'in decimal:',i)