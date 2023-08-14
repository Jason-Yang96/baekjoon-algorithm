# 모든 경우를 구한 다음에 경우의 수를 구하기 때문에 시간 초과가 발생함
from itertools import combinations

def bridge_combination(n:int, r:int):
    n_list = list(range(0, n, 1))
    return len(list(combinations(n_list, r)))
    
N = int(input())
for _ in range(N):
    w, e = map(int, input().split())
    print(bridge_combination(e , w))