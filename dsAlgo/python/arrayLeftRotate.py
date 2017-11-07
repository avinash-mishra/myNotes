#!/usr/bin/env python3
from __future__ import print_function
import platform
import sys
print(platform.python_version())

python_version = sys.version_info.major
print("version is %s"%python_version)
def main():
    # arrLen = int(input("Please input arrLen : "))
    # rotation = int(input("Please input rotation : "))
    arrLen, rotation = map(int, input("Enter arrLen and rotation seperated by space : ").strip().split(' '))
    arr = list(map(int,input("enter all elements of list seperated by space : ").strip().split(' ')))

    print("Entered array is : ")
    print(*arr, sep=' ')

    new_arr = rotationf(arrLen, rotation, arr)
    print("After rotation : ")
    print(*new_arr, sep=' ')

def rotationf(len, n, l):
    return l[n:]+l[:n]
if __name__ == '__main__':main()
