if __name__ == "__main__":
    N = int(input())
    
    i = 1
    j = 0
    n = N
    count = 0
    while True:
        a = int(n / i)
        b = n % i
        if b == 0 and (a-(i-1))>0:
            count+=1
        if (a-(i-1))<0:
            break
        i+=1
        j+=1
        n+=j
    ans = count*2
    print(ans)
            
