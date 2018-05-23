numbers = int(input())
primes = [2]
count = 0
nums = map(int, input().split(' '))

for i in range(3, 1001):
    isPrime = True
    for prime in primes:  
        if i % prime == 0:
            isPrime = False
    if isPrime:
        primes.append(i)

for num in nums:
    if num in primes:
        count += 1

print(count)