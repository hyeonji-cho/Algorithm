import sys
input = sys.stdin.readline

N = int(input()) # 수의 개수 
I = list(map(int, input().split()))
I.sort()

count = 0

# 좋은 수 판별
for n in range(N):
    num = I[n]
    i = 0
    j = N-1
    
    while i<j:
        if I[i] + I[j] < num:
            i += 1
        elif I[i] + I[j] > num:
            j -= 1
        else: # 정답인 경우 
            # num과 같은 경우 제외 
            if i == n:
                i += 1
            elif j == n:
                j -= 1
            else:
                count += 1
                break
            
print(count)