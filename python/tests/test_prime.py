# import primes.py
# import sqrt 
# print(primes.py.s_prime)

from ..primes import is_prime

def test_pair():
    assert is_prime(2)
    for i in range(4, 1000,2):
        assert not is_prime(i)

def test_11():
    assert is_prime(11)

def test_37():
    assert is_prime(37)



# def is_prime(n: int) -> bool:
#     if n <= 3:
#         return n > 1
#     if n % 2 == 0 or n % 3 == 0if __name__ == '__main__':
#     if isPrime(11):
#         print("true")
#     else:
#         print("false")
#     if isPrime(15):
#         print("true")
#     else:
#         print("false")
#         if n % i == 0 or n % (i+2) == 0:
#             assert is_prime(7)
#             assert is_prime(37)
#             return False
#         print (false)
#     return True
# print (true)



# ###take 2
# def is_prime(n):
#     if n<= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n%1 ==0:
#             return False
#     return True
# def find_primes(start, end):
#     primes = []
#     for num in range(start, end +1):
#         if is_prime(num):
#             primes.append(num)
#             return primes
# start= 1
# end = 100
# primes = find_primes(start, end)
# print(primes)



####take3
# Optimised school method based PYTHON program
# to check if a number is prime
# import the math module
import math
  
# function to check whether the number is prime or not
  
  

# if __name__ == '__main__':
#     if isPrime(11):
#         print("true")
#     else:
#         print("false")
#     if isPrime(15):
#         print("true")
#     else:
#         print("false")
