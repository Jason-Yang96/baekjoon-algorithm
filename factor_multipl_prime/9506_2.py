def find_divisor(n:int):
    divisor_list = []
    for divisor_candidate in range(1, int(n**(1/2))+1):
        if n % divisor_candidate == 0:
            divisor_list.append(divisor_candidate)
            if divisor_candidate**2 != n:
                divisor_list.append(n//divisor_candidate)
    divisor_list.sort()
    return divisor_list

while True:
    n = int(input())
    if n == -1:
        break
    if n == sum(find_divisor(n)[:(len(find_divisor(n))-1)]):
        print(str(n) + " = " + ' + '.join(map(str,find_divisor(n)[:(len(find_divisor(n))-1)])))
    else:
        print(f"{n} is NOT perfect.")
