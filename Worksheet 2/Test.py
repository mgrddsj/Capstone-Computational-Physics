# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 20:45:06 2020

@author: Jesse
"""

def findPrimes(n):
    i = 2
    primes = []
    while i * i <= n:
        while n % i == 0:
            primes.append(i)
            n //= i
        i += 1
    if n > 1:
        primes.append(n)
    return primes

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
def mod_inverse(x,y):

	# See: http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
	def eea(a,b):
		if b==0:return (1,0)
		(q,r) = (a//b,a%b)
		(s,t) = eea(b,r)
		return (t, s-(q*t) )

	inv = eea(x,y)[0]
	if inv < 1: inv += y #we only want positive values
	return inv

lines = int(input())

for i in range(lines):
    n, e = input().split()
    n = int(n)
    e = int(e)
    
    primes = findPrimes(n)
    t = (primes[0]-1) * (primes[1]-1)
    
#    d = 0
#    while e*d%phi != 1:
#        d += 1
    d = mod_inverse(e, t)
    
    
    print(d)