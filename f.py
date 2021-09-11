import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n1 = int(input())
n2 = 0
 
while n1 > 0:
    number = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + number  
 
print(n2)