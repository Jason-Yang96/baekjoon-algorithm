""" 
ZZZZZ = 35*36**4 + 35*36**3 + 35*36**2 + 35*36**1 + 35
"""
# 직접 10진법 전환
def base_n(a, b):
    input_list = list(a)
    sum_list = []
    for i in range(len(input_list)):
        if input_list[i].isalpha():     
            digit = ord(input_list[i]) - 55
            sum_list.append(digit*int(b)**(len(input_list)-i-1))
        else:
            sum_list.append(int(input_list[i])*int(b)**(len(input_list)-i-1))
    return sum(sum_list), sum_list
n, base = input().split()

print(base_n(n, int(base))) 

# int() 함수 활용 10진법 전환 방법
def base_n(a, b):
    return int(a,b)

n, base = input().split()
print(base_n(n, int(base)))



