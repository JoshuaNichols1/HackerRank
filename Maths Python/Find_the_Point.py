import os


def findPoint(px, py, qx, qy):
    my = (qy - py)
    mx = (qx-px)
    return (qx + mx), (qy + my)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        pxPyQxQy = input().split()

        px = int(pxPyQxQy[0])

        py = int(pxPyQxQy[1])

        qx = int(pxPyQxQy[2])

        qy = int(pxPyQxQy[3])

        result = findPoint(px, py, qx, qy)
        print(result)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
