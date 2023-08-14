# input 보다 더 빠르게 값 불러들이는 방법, 백준 결과 동일 메모리 사용시에 더 짧은 시간 사용(44ms < 76ms)
import math
import sys

N = int(sys.stdin.readline().rstrip()) 
for _ in range(N):
    r, n = map(int, sys.stdin.readline().rstrip().split())
    n = int(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))
    print(n)