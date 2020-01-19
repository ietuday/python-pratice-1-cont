#!/usr/bin/env python3

def insertion_sort(arr):
    for index in range(1, len(arr)):
        key = arr[index]
        start = index - 1
        while start >= 0 and arr[start] > key:
            arr[start + 1] = arr[start]
            start -= 1
        arr[start + 1] = key
    return arr

def main():
    arr = [int(ele) for ele in input().split()]
    print('Sorted array :', insertion_sort(arr))

if __name__ == '__main__':
    main()
