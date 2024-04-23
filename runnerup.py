if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    totmax = max(arr)
    currmax = float("-inf")
    for i in range(len(arr)):
        if arr[i] > currmax and arr[i] < totmax:
            currmax = arr[i]
    print(currmax)