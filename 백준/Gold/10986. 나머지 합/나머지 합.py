import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # N, M

# 원본 배열 입력받기
numbers = map(int, input().split())
    
# 합 배열 구하기
total_sum = []
current_num = 0
for i in numbers: # M번 반복
    current_num += i
    total_sum.append(current_num)
    
# 합 배열에 % 연산 수행 
C = [0] * M
answer = 0
for i in range(N):
    remainder = total_sum[i] % M
    if remainder == 0:
        answer += 1 
    C[remainder] += 1 # 나머지가 같은 인덱스의 개수 값 증가 

# 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수 더하기    
for i in range(M):
    if C[i] > 1:
        answer += (C[i] * (C[i]-1) // 2)
        
print(answer)