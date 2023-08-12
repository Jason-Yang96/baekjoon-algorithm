""" 
1(1) -> 2~7(6) -> 8~19(12) -> 20~37(18) -> 38~61(24)
 
1+6+12
 """
def room_pass_count(n: int):
    sum = 1
    count = 1
    while n > sum:
        sum += 6*count
        count += 1
    return count

n = int(input())
print(room_pass_count(n))