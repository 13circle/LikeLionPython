def isPrime(n):
    i = n - 1
    while(i > 1 and n % i != 0):
        i = i - 1
    if i == 1:
        return True
    return False

def primeNlist(l):
    r = []
    n = 2
    while(len(r) != l):
        if(isPrime(n)):
            r.append(n)
        n = n + 1
    return r

print(primeNlist(int(input('# of primes: '))))