import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # N, M
numbers = list(map(int, input().split())) # N개의 수 입력받기
total_sum = [0] # 합 배열

# 합 배열 채우기 
current_num = 0
for i in numbers: # M번 반복
    current_num += i
    total_sum.append(current_num)
    
# 구간 합 구하기 
for i in range(M):
    start, end = map(int, input().split())
    print(total_sum[end] - total_sum[start-1])