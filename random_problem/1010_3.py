import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N, M = map(int,input().split())
    a = 1
    b = 1
# 팩토리얼을 굳이 내장함수 사용하지 않고 직접 구현, 조합에 대한 정확한 이해 필요
    for i in range(M, M-N,-1):
        a *= i
    
    for j in range(N,1,-1):
        b *= j
    print(int(a/b))