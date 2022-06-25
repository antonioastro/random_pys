def CheckPrime(n):
    primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if n%2==0:
        return False
    else:
        m=n**0.5
        for item in primes: 
            if item<=m and n%item==0:
                return False
            else:
                continue
            
list=[]

for n in range(1,10000):
    if CheckPrime(n)!=False:
        list.append(n)
    else:
        continue