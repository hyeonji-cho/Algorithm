import sys
input = sys.stdin.readline

N = int(input()) # N 입력받기 
count = 1
start = 1
end = 1
sum = 1 

while end != N:
    if sum == N: # 정답인 경우 
        count += 1
        end += 1
        sum += end
    elif sum < N: # 합이 정답보다 작은 경우 
        end += 1
        sum += end
    else: # 합이 정답보다 큰 경우 
        sum -= start
        start += 1
        
print(count)