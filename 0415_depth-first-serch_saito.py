class stack:
    """
    original stack class.
    """
    def __init__(self):
        self.stack = []
    def push(self,item):
        return self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return self.stack==[]
    def size(self):
        return len(self.stack)
    def top(self):
        return self.stack[-1]

def next(u):
    for v in range(nt[u],N):
        nt[u] = v + 1
    # for v in range(0,N):
        if M[u][v] !=0 :
            return v
    return -1

if __name__ == "__main__":
    N = 6
    data = [[1,2,2,3],[2,2,3,4],[3,1,5],[4,1,6],[5,1,6],[6,0]]

    M = [[0 for j in range(N)] for i in range(N)]
    for i in range (N):
        if data[i][1] != 0:
            d = data[i][1]
            for j in range (2,2+d):
                M[i][data[i][j]-1] = 1
    print(M)

    color = [0]*N
    d = [0]*N
    f = [0]*N
    s = stack()
    time = 1

    nt = [0]*N

    s.push(0)
    color[0] = 1
    d[0] = time
    while not(s.is_empty()):
        u = s.top()
        v = next(u)
        if v != -1:
            if color[v] == 0:
                color[v] = 1
                time += 1
                d[v] = time
                s.push(v)
        else:
            s.pop()
            color[u] = 1
            time += 1
            f[u] = time


    print("output:{}".format(d))
    print("output:{}".format(f))

    