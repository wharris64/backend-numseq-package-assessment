def primes(n):
    prime_list = []    
    for i in range(n):
        if is_prime(i):
            prime_list.append(i)
    return prime_list



                    
            
def is_prime(n):
    if n <= 1: 
        return False
    if n <= 3 and n > 1: 
        return True
    
    if n % n == 0 or n % 1 == 0: 
        for i in range(2, n):
            if n % i == 0:
                return False
            else:
                return True


            
        
  
    return True