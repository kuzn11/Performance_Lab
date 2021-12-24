import sys

def calculation(n,m):
    i = 1
    while True:
        print(i, end='')
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    print()

if __name__ == '__main__':
    if sys.argv and len(sys.argv) > 2:
        n = sys.argv[1]
        m = sys.argv[2]
    else:
        n, m = map(int, input().split())
    calculation(n, m)
