# 숫자 입력
N = int(input())
# 도화지 2차원 배열화
board_range = [[0]*100 for _ in range(100)]
# 첫줄에 주어진 숫자만큼 반복
for _ in range(N):
    col, row = map(int, input().split()) 
    # 10개가 1로 변환되어야 한다
    for i in range(row, row + 10):
        for j in range(col, col+10):
            board_range[i][j] = 1  

# 면적 전역 변수 설정 
area = 0
for row_check in range(100):
    area += board_range[row_check].count(1)

print(area)