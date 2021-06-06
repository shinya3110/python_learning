
if __name__ == "__main__":
    nw = input()
    NW = nw.split()
    NW = [int(x) for x in NW]
    N = NW[0]
    W = NW[1]

    T = []
    for i in range(N):
        a = input()
        A = a.split()
        A = [int(x) for x in A]
        T.append(A)
    MAX = max(max(T))
    MIN = min(min(T))


    A = [[0] * (MAX+1) for i in range(N)]
    for i in range(N):
        for j in range(T[i][0],T[i][1]):
            A[i][j] = T[i][2]

    Sum = 0
    tmp = 1
    for i in range (MAX+1):
        for j in range(N):
            Sum += A[j][i]
        if Sum > W:
            tmp = 0
            break
        Sum = 0
    if tmp == 0:
        ans = str("No")
    else:
        ans = str("Yes")
    print(ans)

