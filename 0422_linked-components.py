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
        if vlist[u][v] != 0 :
            return v
    return -1


if __name__ == "__main__":
    N = 10
    e = 9
    data = [[0,1],[0,2],[3,4],[5,7],[6,7],[6,8],[7,8],[8,9]]

    vlist = [[] for i in range(N)]

    for i in range(8):
        vlist[data[i][0]].append(data[i][1])
        vlist[data[i][1]].append(data[i][0])

    print(vlist)

    start = 0
    end = 1

    color = [0]*N
    s = stack()
    nt = [0]*N

    s.push(start)
    color[start] = 1
    while not(s.is_empty()):
        u = s.top()
        for i in range(len(vlist[u])):
            v = vlist[[u][i]]
            if v == end:
                print('yes')
            s.push(v)
        else:
            s.pop()
            color[u] = 1
