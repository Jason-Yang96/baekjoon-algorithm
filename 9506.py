"""코드 재사용_잘 짜여진 코드는 재사용이 가능하다"""
"""class와 method를 잘 사용하자..."""
""" class PerfectNum:
    def __init__(self, N:int):
        self.N = N
    
    def find_divisor(self):
        divisor_stack_list = []
        for divisor_candidate in range(1,self.N+1):
            if self.N % divisor_candidate  == 0:
                divisor_stack_list.append(divisor_candidate)
            else: 
                pass
        return divisor_stack_list
    
    def judge_perfect_num(self, stack_list: list):
        self.divosr_list = self.find_divisor()
        if sum(self.divosr_list[:self.N]) == self.N:
            return print(f"{self.N} = ", *)
        else:
            return print(f"{self.N} is Not perfect") """
# let's make dirty code for speed and then pursue perfect
def find_divisor_without_self(n: int):
    divisor_list = []
    for divisor_candidate in range(1, n):
        if n % divisor_candidate == 0:
            divisor_list.append(divisor_candidate)
        else:
            pass
    return divisor_list

while True: 
    n = int(input())
    if n == -1:
        break
    if n == sum(find_divisor_without_self(n)):
        print(str(n) + " = " + ' + '.join(map(str,find_divisor_without_self(n))))
    else:
        print(f"{n} is NOT perfect.")
    