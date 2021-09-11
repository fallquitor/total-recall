import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n=int(input())
a = [int(s) for s in input().split()]
for i in range(n):
    if a[i] % 2 == 0:
        print(a[i], end=' ')
for i in range(n):
    if a[i] % 2 != 0:
        print(a[i], end = ' ')