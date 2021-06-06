import math

if __name__ == "__main__":
    xyab = input()
    XYAB = xyab.split()
    XYAB = [int(x) for x in XYAB]
    X = XYAB[0]
    Y = XYAB[1]
    A = XYAB[2]
    B = XYAB[3]

    cnt = 0
    if X+B <= X*A:
        cnt = math.floor(Y/B)
    else:
        tmp = X*A
        cnt+=1
        while True:
            if tmp+B <= tmp*A:
                tmp = tmp/A
                break
            else:
                tmp=tmp*A
                cnt+=1
        
        dif = 0
        dif = math.floor((Y-tmp)/B)
        cnt = cnt + dif -1

    print(cnt)


