def mersenne(n): #a mersenne number is one less than a power of 2
    return (2**n) -1

def lehmer(n): #a lucas-lehmer number is generated from a series where s1=4, and each subsequent number is the previous squared subtract 2
    if n==0:
        x=4 #the zeroth lehmer number is 4
        return x
    else:
        m=1
        x=4
        while m<n: #this while loop is messy and could probably be better
            x = x**2-2
            m+=1
        return x
        
def prime_check(n): #to check a mersenne number 2^n-1 is a prime, divide the lehmer number for n-1 by it, and the remainder is 0 if it is a prime
    if lehmer(n-1)%mersenne(n)==0:
        return True
    else:
        return False

n=1
while n<32:
    print('Mersenne number', 2**n-1,'(n=',n,') Is_A_Prime=',prime_check(n))
    n+=1