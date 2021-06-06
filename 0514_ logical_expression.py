import itertools

if __name__ == "__main__":
    N = int(input())
    s = input()
    S = s.split()
    S = [str(x) for x in S]

    x = []
    seq = ('True', 'False')
    list(itertools.product(seq, seq))

    print(list)
