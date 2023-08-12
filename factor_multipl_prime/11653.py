N = int(input())
if N == 1:
    print('')
    
while N % 2 == 0:
    N = N // 2
    print(2)
    
for i in range(3, N + 1, 2):
    while N % i == 0:
        N = N // i 
        print(i)