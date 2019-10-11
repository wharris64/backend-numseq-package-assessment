from numseq.fib import fib
from numseq.geo import *
from numseq.prime import *
import sys
# import timeit
"""[runs modules]
"""

def main():
    """[implements test code to test the functions against and measures run time]
    """
    print ("Fibonacci")
    for i in range(10):
        print ("{}: {}".format(i, fib(i)))

    print("Geometric numbers (square, triangle, cube)")
    for i in range(10):
        print ("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))

    print ("Primes")
    prime_list = primes(1000)
    for p in prime_list[-10:]:
        print (p)
    print ("Is 999981 prime? {}".format(is_prime(999981)))
    print ("Is 999983 prime? {}".format(is_prime(999983)))
   
    print("program ran in {} seconds".format())



if __name__ == "__main__":
    main()