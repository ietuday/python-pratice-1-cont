#!/usr/bin/env python3

def binary_search(arr, item):
    beg = 0
    end = len(arr) - 1
    while beg <= end:
        mid = beg + end // 2
        if arr[mid] == item:
            return (mid + 1)
        elif arr[mid] < item:
            beg = mid + 1
        else:
            end = mid - 1
    return -1


def main():
    arr = [int(ele) for ele in input().split()]
    ele = int(input())
    print(ele, 'found at', binary_search(arr, ele), 'position')

if __name__ == '__main__':
    main()
