from numseq.fib import fib
from numseq.geo import *
from numseq.prime import *
import sys
import datetime
import timeit
"""[runs modules]
"""

def main():
    """[implements test code to test the functions against and measures run time]
    """
    start = datetime.datetime.now()
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
    end = datetime.datetime.now()
    run_time = end - start
    print("program ran in {} seconds".format(run_time))

# def timeit_helper_fib():
#     """[helper function to measure time to complete program]
#     """
#     t = timeit.Timer(stmt="main('')",
#                      setup='from __main__ import find_duplicate_movies')
#     number_of_tests = 7
#     runs_per_test = 3
#     result_list = t.repeat(number_of_tests, runs_per_test)
#     per_func_cost = min(result_list)/runs_per_test
#     # print "Best time across {} tests of {} runs per test: {:.02f}".format(
#     #     number_of_tests, runs_per_test, per_func_cost
#     # )

if __name__ == "__main__":
    main()