if __name__ == "__main__":
    data = [[-1,2,3,1,-1],[2,-1,-1,4,-1],[3,-1,-1,1,1],[1,4,1,-1,3],[-1,-1,1,3,-1]]
    rslt = [1]
    w = []

    # while len(rsle)!=5:
    tmp = 10
    index = 0
    for l in range(5):
        for i in range (len(rslt)):
            for j in range (0,4):
                if data[rslt[i]-1][j] >= 0 and tmp >= data[rslt[i]-1][j]:
                    tmp = data[rslt[i]-1][j]
                    index = j
        data[rslt[i]-1][index] = -1
        data[index][rslt[i]-1] = -1
        rslt.append(index+1)
        w.append(tmp)

    # print(tmp)
    # print(index)
    print(data)
    print("木:" + str(rslt))
    ans = sum(w)
    print('w:' + str(w))
    print("総和:" + str(ans))
    print(rslt)
    