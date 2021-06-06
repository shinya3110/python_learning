import math

if __name__ == "__main__":
    nm = input()
    a = input()
    NM = nm.split()
    A = a.split()
    NM = [int(x) for x in NM]
    A = [int(x) for x in A]
    N = NM[0]
    M = NM[1]
    B = sorted(A)

    if B!=[]:
        d = []
        i = 0
        tmp = B[i]-1
        if tmp!=0:
            d.append(tmp)
        i+=1
        while True:
            if i<=M-1:
                tmp = B[i]-B[i-1]-1
                if tmp!=0:
                    d.append(tmp)
                i+=1
            else:
                break
        tmp = N-B[i-1]
        if tmp!=0:
            d.append(tmp)

        ans = 0
        if d==[]:
            print(ans)
        else:
            MIN = min(d)
            for i in range(len(d)):
                c = math.ceil (d[i] / MIN)
                ans+=c
            print(ans)
    else:
        ans=1
        print(ans)

    
