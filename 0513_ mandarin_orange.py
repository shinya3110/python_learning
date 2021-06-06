import random
import string
import copy

def merge(data,left,right):
    mid = int( (left+right) / 2 )
    n1 = mid - left
    n2 = right - mid
    leftData = [ data[0][i+left] for i in range(n1) ]
    leftData_str = [ data[1][i+left] for i in range(n1) ]

    rightData = [ data[0][i+mid] for i in range(n2) ]
    rightData_str = [ data[1][i+mid] for i in range(n2) ]
    i = 0
    j = 0
    leftData.append(float("inf"))
    rightData.append(float("inf"))

    for k in range(left,right):
        if leftData[i] <= rightData[j]:
            data[0][k] = leftData[i]
            data[1][k] = leftData_str[i]
            i += 1
        else:
            data[0][k] = rightData[j]
            data[1][k] = rightData_str[j]
            j += 1
 
def mergeSort(data,left,right):
    if left + 1 < right:
        mid = int( (left+right) / 2 )
        mergeSort(data,left,mid)
        mergeSort(data,mid,right)
        merge(data,left,right)


if __name__ == "__main__":
    N = int(input())
    a = input()
    A = a.split()
    A = [int(x) for x in A]
    index = []
    for i in range(N):
        index.append(i)

    input_data = []
    input_data.append(A)
    input_data.append(index)

    output2=copy.deepcopy(input_data)
    mergeSort(output2,0,len(output2[0]))
    output2[0].reverse()
    output2[1].reverse()
    print(output2)