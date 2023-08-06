# A 올라가고 B 내려간다. V 이상은 가야 한다. 며칠이 걸리나? 
# A가 V보다 크면 바로 탈출. day = 1 부터 시작
# V가 A보다 크거나 같으면 
# 1: 2 -1 2: 2 -1 3: 2 -1 4: 2 
""" import time
start = time.time()
def day_count(up: int, down: int, remained_height: int) -> int:
    day = 0
    while True:
        move = up - down
        remained_height -= move
        day += 1
        if up >= remained_height:
            break
    return day + 1 
        
A, B, V = map(int, input().split())
start = time.time()
print(day_count(A, B, V))
end = time.time()
print(end - start) """

""" def day_count(up: int, down:int, remained_height: int) -> int:
    quetient, remainder = divmod(remained_height, up-down)
    day = remained_height - up + 1
    return day

A, B, V = map(int, input().split())
print(day_count(A, B, V))
 """
A, B, V = map(int, input().split())

if (V-B) % (A-B) == 0 :
    print((V-B)//(A-B))
else:print((V-B)//(A-B)+1)

   
