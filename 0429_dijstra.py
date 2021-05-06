if __name__ == "__main__":
    N = 5
    a = [-1,2,3,1,-1]
    b = [2,-1,-1,4,-1]
    c = [3,-1,-1,1,1]
    d = [1,4,1,-1,3]
    e = [-1,-1,1,3,-1]

    data = []
    data.append(a)
    data.append(b)
    data.append(c)
    data.append(d)
    data.append(e)

    d = [1000]*(N)
    p = [0]*(N)

    u = 0
    d[u] = 0
    for i in range (N):
        tmp = 100
        for j in range (N):
            if data[u][j] >= 0:
                v = j            
                if d[u] + data[u][j] < d[v]:
                    d[v] = d[u] + data[u][j]
                    p[v] = u
                if tmp > data[u][j]:
                    tmp = data[u][j]
                    index = j
        data[index][u] = -1
        u = index
    print(d)
    print(p)




    # tmp = 100
    # for i in range (N):
    #     for j in range (N):
    #         if data[u][j] >= 0 and tmp > data[u][j]:
    #             tmp = data[u][j]
    #             index = j
    #     data[index][u] = -1
    #     v = index
        
    #     if d[u] + tmp < d[v]:
    #         d[v] = d[u] + w
    #         p[v] = u
