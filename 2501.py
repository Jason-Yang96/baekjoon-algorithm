""" N과 K가 주어진다. 뭐가 더 크지?(이미 문제 조건에서 주어짐) 
설계에서 이거 걸러지면 좋겠고, K번째 약수가 없다면? 약수 개수가 K개 보다 적을 수 있잖아. 이건 중간에 걸러주자. 0 반환 해주면 되지 """
def find_nth_divisor(N: int, K: int ):
    divisor_stack_list = []
    for divisor_candidate in range(1,N+1):
        if N % divisor_candidate  == 0:
            divisor_stack_list.append(divisor_candidate)
        else: 
            pass
    if K <= len(divisor_stack_list):
        return divisor_stack_list[K-1]
    else: 
        return 0

input_N, input_K = map(int, input().split())
print(find_nth_divisor(input_N, input_K))