""" 
124센트가 주어지면 25센트로 먼저 나눠서 몫과 나머지를 구하고 나머지를 10센트로 나눠서 몫과 나머지를 구하고 나머지를 5센트로 나눠서 몫과 나머지를 구하고 마지막은 
1센트로 나눠서 몫과 나머지를 구해주면 된다. 
진법 전환과 다른 점은 나눠주는 값이 차례로 변한다는 점이고 출력해야 하는 숫자가 몫이라는 점이다. 
""" 
from typing import Any
def change_count(cent: int) -> Any:
    cent_list = [25, 10, 5, 1]
    count = []
    for i in cent_list:
        # 몫, 나머지
        n, cent = divmod(cent, i)
        count.append(n)
    return print(*count)

N = int(input())
for _ in range(N):
    cent_input = int(input())
    change_count(cent_input)
