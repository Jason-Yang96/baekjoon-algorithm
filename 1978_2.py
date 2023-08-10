def prime_judge(n: int):
    if n == 1:
        return False
    else:
        for j in range(2, int(n ** 1/2)+1):
            if n % j == 0: 
                return False
        return True

input()
input_list = list(map(int, input().split()))
cont = 0
for i in input_list:
    if prime_judge(i):
        cont += 1

print(cont)

