def prime_judge(a: int):
    if a == 1:
        return False
    for i in range(2, int(a**(1/2))+1):
        if a % i == 0:
            return False
    return True
    
start_num = int(input())
end_num = int(input())
prime_list = []

for i in range(start_num, end_num+1):
    if prime_judge(i):
        prime_list.append(i)
        
if len(prime_list) == 0:
    print(-1)
else:
    print(prime_list[0])
    print(sum(prime_list))