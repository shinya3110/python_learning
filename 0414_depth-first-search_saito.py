if __name__ == '__main__':

    n = 4

    data=[[1,2,3,4],[2,1,3],[3,0],[4,3,1,2,3]]
    r = [[0 for j in range(n)] for i in range(n)]

    for i in range (n):
        if data[i][1] != 0:
            num = data[i][1]
            for j in range (2,2+num):
                r[i][data[i][j]-1] = 1
    
    for i in range (n):
        print(int(r[i][0]),str(" "),int(r[i][1]),str(" "),int(r[i][2]),str(" "),int(r[i][3]))  



