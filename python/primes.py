
# def is_prime(n):
#     print(f"Number is {n}")
#     return False
import math

def is_prime(n):
    #1 is not prime since definition is divisible by themselves, and one and must be bigger than one.
    if (n <= 1):
        return False #They are not then
  
    #compute
    for i in range(3, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True
  
  

if __name__ == '__main__':
    import sys
    print(is_prime(int(sys.argv[1])))
