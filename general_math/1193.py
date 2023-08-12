# 1 -> 3 -> 6 -> 10 -> 
def find_fraction(n: int):
    set_n = 1
    set_len = 1
    while n > set_len:
        set_n +=1 
        set_len += set_n
    if set_n % 2: 
       answer =  f"{str(1 + (set_len-n))}/{str(set_n -(set_len-n))}"
    else:
       answer =  f"{str(set_n -(set_len-n))}/{str(1 + (set_len-n))}"
    return answer

n = int(input())
print(find_fraction(n))