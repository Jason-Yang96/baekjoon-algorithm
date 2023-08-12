#소수 약수가 자기 자신 말고 1밖에 없는 애들. 소수 판별기 필요. counter 필요. 
def prime_judge(n: int):
    if n == 2:
        return True
    elif (n == 1) | (n % 2 == 0) :
        return False
    else:
        for i in range(3, n):
            if n % i == 0 :
                return False
            else:
                pass
        return True
 
N = int(input())
input_list = list(map(int, input().split()))
counter = 0
for i in input_list:
    if prime_judge(i):
        counter += 1
        
print(counter)