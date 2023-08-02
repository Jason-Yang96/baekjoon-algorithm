def solution(number, base):
    reversed_base = ''

    while number > 0:
        number, r = divmod(number, base)
        if r > 9:
            r = chr(55+r)
        reversed_base += str(r)

    return reversed_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

N, B = map(int, input().split())

print(solution(N, B))  



