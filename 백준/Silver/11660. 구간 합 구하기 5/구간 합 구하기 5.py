import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # N, M

# 원본 배열 입력받기
numbers = [[0] * (N+1)]
for i in range(N):
    row = [0] + list(map(int, input().split()))
    numbers.append(row)
    
# 합 배열 구하기
s = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        s[i][j] = s[i][j-1] + s[i-1][j] - s[i-1][j-1] + numbers[i][j]

# M번 반복
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1]
    print(result)