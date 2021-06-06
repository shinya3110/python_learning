if __name__ == "__main__":
    n = input()
    N = int(n)
    a = input()
    A = a.split()
    A = [int(x) for x in A]

    MOD=1000000007
    all = sum(A)
    ans = 0
    for i in range(N-1):
        all = all-A[i]
        b = A[i]*all
        ans = ans+b

    print(ans%MOD)