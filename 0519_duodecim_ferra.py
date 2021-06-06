import math

if __name__ == "__main__":
    N = int(input())
    
    n = N-1
    r = 11
    a = math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    
    print(a)
