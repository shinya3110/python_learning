import itertools

if __name__ == "__main__":
    nm = input()
    NM = nm.split()
    NM = [int(x) for x in NM]
    N = NM[0]
    K = NM[1]

    T = []
    for i in range(N):
        a = input()
        A = a.split()
        A = [int(x) for x in A]
        T.append(A)

    b = []
    for i in range(N-1):
        j = i+2
        b.append(j)
    B = len(b)
    
    count = 0
    for per in itertools.permutations(b):
        j = 0
        tmp = 0
        d = []
        for i in range (B):
            tmp = T[j][list(per)[i]-1]
            d.append(tmp)
            j = list(per)[i]-1
        d.append(T[j][0])
        if sum(d) == K:
            count+=1
    print(count)

        

