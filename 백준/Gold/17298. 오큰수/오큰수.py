import sys
input = sys.stdin.readline

N = int(input()) # 수열의 크기

A = list(map(int, input().split()))
ans = [-1] * N # -1로 초기화 
stack = [0]

for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i] # 정답 리스트에 오큰수를 현재 수열로 저장
    stack.append(i)
    
for i in range(N):
    print(str(ans[i]), end=" ")