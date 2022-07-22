def enum(arr):
    for i in range(len(arr)):
        yield (i, arr[i])


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i, e in enum(a):
        print(i, e)
