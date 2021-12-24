import sys
def get_data():
    if sys.argv and len(sys.argv) > 1:
        file = sys.argv
    else:
        name = input()
        file = name

    with open(file, 'r') as f:
        return [int(x) for x in f.read().strip('[]\n').split('\n')]

def nearest(lst):
    sr_znach = sum(data) // len(data)
    return min(lst, key=lambda x: abs(x-sr_znach))

def operations(data):
    ans = 0
    for item in range(len(data)):
        ans = ans+ abs(data[item]-nearest(data))
    return(ans)

if __name__ == '__main__':
    data = get_data()
    print(operations(data))

