#!/usr/bin/env python3

def linear_search(arr, ele):
    for idx, item in enumerate(arr):
        if item == ele:
            return (idx + 1)

def main():
    arr = [int(ele) for ele in input().split()]
    ele = int(input())
    print(ele, 'found at :', linear_search(arr, ele), 'position.')

if __name__ == '__main__':
    main()
