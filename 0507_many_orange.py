import math

if __name__ == "__main__":
    nl = input()
    NL = nl.split()
    NL = [int(x) for x in NL]

    A = NL[0]
    B = NL[1]
    w = NL[2]
    W = w * 1000
    num1 = math.floor(W / A)
    num2 = math.floor(W / B)


    j = 0
    ans = []
    for i in range (num1):
        while j <= num2:
            SUM = A*(num1-i) + B*j
            div = abs(W - SUM)
            if div<=B-A:
                num = (num1-i) + j
                ans.append(num)
            j+=1
            if SUM > W:
                break
        j = ０

    if ans==[]:
        print("UNSATISFIABLE")
    else:
        ans1 = min(ans)
        ans2 = max(ans)
        print(str(ans1) + " " + str(ans2))

    # j = 0
    # ans = []
    # for i in range (num1):
    #     while j <= num2:
    #         SUM = A*(num1-i) + B*j
    #         div = abs(W - SUM)
    #         if div<=B-A:
    #             num = (num1-i) + j
    #             ans.append(num)
    #         j+=1
    #         if SUM > W and SUM < W-A:
    #             break
    #     j = 0





    # j = 0
    # ans = []
    # for i in range (num1):
    #     while j <= num2:
    #         SUM = A*(num1-i) + B*j
    #         div = abs(W - SUM)
    #         if SUM <= W:
    #             if W <= SUM+div:
    #                 num = (num1-i) + j
    #                 ans.append(num)
    #             else:
    #                 j+=1
    #                 break
    #         else:
    #             break
