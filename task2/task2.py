import sys

def serch_point(x_cercle, y_cercle, r, x_point, y_point):
        if ((x_point - x_cercle) ** 2 + (y_point - y_cercle) ** 2) == (r ** 2):
            print('0')
        elif ((x_point - x_cercle)**2 + (y_point -  y_cercle)**2) < (r**2):
            print('1')
        elif ((x_point - x_cercle)**2 + (y_point -  y_cercle)**2) > (r**2):
            print('2')
        return

if __name__ == '__main__':
    if sys.argv and len(sys.argv) > 2:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
    else:
        names = input()
        file1, file2 = names.split(' ')
    with open(file1, 'r') as file1:
        x_cercle, y_cercle = map(float, file1.readline().split())
        r = float(file1.readline())
    with open(file2, 'r') as file2:
        for line in file2:
            x_point, y_point = map(float, line.split())
            serch_point(x_cercle, y_cercle, r, x_point, y_point)


