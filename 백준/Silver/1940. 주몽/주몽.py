import sys
input = sys.stdin.readline

N = int(input()) # 재료의 개수 
M = int(input()) # 갑옷을 만드는 데 필요한 수 

# N개 재료들의 고유한 번호
I = list(map(int, input().split()))
I.sort()

count = 0
# 투 포인터
i = 0
j = N-1

# 탐색 수행 
while i<j:
    if I[i] + I[j] < M:
        i += 1
    elif I[i] + I[j] > M:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)