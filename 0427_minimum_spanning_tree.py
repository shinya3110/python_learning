if __name__ == "__main__":
    data = [[-1,2,3,1,-1],[2,-1,-1,4,-1],[3,-1,-1,1,1],[1,4,1,-1,3],[-1,-1,1,3,-1]]
    rslt = [1]
    w = []

    tmp = 10
    index = 0
    n = 0
    for l in range(4):
        for i in range (len(rslt)):
            for j in range (0,5):
                if data[rslt[i]-1][j] >= 0 and tmp >= data[rslt[i]-1][j]:
                    tmp = data[rslt[i]-1][j]
                    index = j
                    n = rslt[i]
        data[n-1][index] = -1
        data[index][n-1] = -1
        rslt.append(index+1)
        w.append(tmp)
        tmp = 10
        index = 0
        n = 0

    # print(data)
    print("木:" + str(rslt))
    ans = sum(w)
    # print('w:' + str(w))
    print("総和:" + str(ans))
    # print(rslt)