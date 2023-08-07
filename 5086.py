# 3가지 출력, 첫번째가 두번째의 약수인지, 배수인지, 아무것도 아닌지
def print_factor_multiple (first: int, second: int) -> str:
    if first // second == 0:
        if second % first == 0:
            return "factor"
        else:
            return "neither"
    else:
        if first % second == 0:
            return "multiple"
        else:
            return "neither"

while True:
    first_num, second_num = map(int, input().split())
    if first_num == 0:
        break
    else:
        print(print_factor_multiple(first_num, second_num))
