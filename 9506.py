def find_divisor_without_self(n: int):
    divisor_list_without_self = []
    for divisor_candidate in range(1, n):
        if n % divisor_candidate == 0:
            divisor_list_without_self.append(divisor_candidate)
        else:
            pass
    return divisor_list_without_self

while True: 
    n = int(input())
    if n == -1:
        break
    if n == sum(find_divisor_without_self(n)):
        print(str(n) + " = " + ' + '.join(map(str,find_divisor_without_self(n))))
    else:
        print(f"{n} is NOT perfect.")

