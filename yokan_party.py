if __name__ == "__main__":
    
    nl = input()
    k = input()
    a = input()

    NL = nl.split()
    NL = [int(x) for x in NL]
    N = NL[0]
    L = NL[1]
    K = int(k)
    A = a.split()
    A = [int(x) for x in A]

    s = (L / (K+1))
    tmp_div = []

    S = s
    for i in range (K+1):
        tmp_div.append(S)
        S += s
    # print("tmp_div= " + str(tmp_div))

    count = 0
    tmp1 = 0
    tmp2 = 0
    div = [0]
    for i in range (N):
        if A[i] <= tmp_div[count]:
            tmp1 = A[i]
        else:
            tmp2 = A[i]
            if (tmp_div[count]) - tmp1 < tmp2 - (tmp_div[count]):
                div.append(tmp1)
            else:
                div.append(tmp2)
            tmp1 = tmp2
            count += 1
    div.append(L)
    # print("div= " + str(div))

    reslt = []
    for i in range (len(div)-1):
        rsl = div[i+1] - div[i]
        reslt.append(rsl)
    # print("reslt= " + str(reslt))
    ans = min(reslt)
    print(ans)




