import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
# Решение задачи

for i in range(5):
    (h,m,s) = [int(s) for s in input().split()]
    if h <= 23 and m <= 60 and s <= 60:
        print("YES")
    else:
        print("NO")