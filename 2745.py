""" 
ZZZZZ = 35*36**4 + 35*36**3 + 35*36**2 + 35*36**1 + 35
"""
""" def base_n(a, b):
    sum_list = []
    for i in range(len(a)):
        digit = ord(a[i]) - 55
        sum_list.append(digit*int(b)**(len(a)-i+1))
    return sum(sum_list), sum_list
n, base = input().split()

print(base_n(n, int(base))) """

def base_n(a, b):
    return int(a,b)

n, base = input().split()
print(base_n(n, int(base)))



