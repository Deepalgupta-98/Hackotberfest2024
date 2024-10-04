# Python program for the above approach

import math

# Function to check if a number n is a prime number of not
def isPrime(n):
	# Edges Cases
	if n <= 1:
		return False

	if n <= 3:
		return True

	# To skip middle five numbers
	if n % 2 == 0 or n % 3 == 0:
		return False

	# Checks for prime or non prime
	for i in range(5, int(math.sqrt(n)) + 1, 6):
		# If n is divisible by i or i + 2, return false
		if n % i == 0 or n % (i + 2) == 0:
			return False

	# Otherwise, the number is prime
	return True

# Function to segregate the primes and non-primes present in an array
def segregatePrimeNonPrime(arr, N):
	# To store Prime Numbers
	prime = []
	# To store non-prime numbers
	nonPrime = []

	# Traverse the input array
	for i in range(N):
		if isPrime(arr[i]):
			prime.append(arr[i])
		else:
			nonPrime.append(arr[i])

	# First print all prime numbers
	for i in range(len(prime)):
		print(prime[i], end=" ")

	# After printing all prime numbers print all non-prime numbers
	for i in range(len(nonPrime)):
		print(nonPrime[i], end=" ")

# Driver Code
if __name__ == '__main__':
	arr = [2, 3, 4, 6, 7, 8, 9, 10]
	N = len(arr)

	segregatePrimeNonPrime(arr, N)
