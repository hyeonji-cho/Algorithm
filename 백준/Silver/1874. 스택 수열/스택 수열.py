import sys
input = sys.stdin.readline

N = int(input())
A = []

# 수열 리스트 채우기
for i in range(N):
    A.append(int(input()))

stack = []
count = 1
result = True
answer = []

for i in range(N):
    su = A[i]
    while su >= count: # 현재 수열값 >= 자연수
        stack.append(count)
        answer.append('+')
        count += 1
        
    # 스택이 비어 있지 않으면서, 스택 가장 위의 수가 만들어야 하는 수열의 수와 같을 때
    if stack and stack[-1] == su:
        stack.pop()
        answer.append('-')
    # 스택이 비어 있지 않으면서, 스택 가장 위의 수가 만들어야 하는 수열의 수보다 크면
    elif stack and stack[-1] > su:
        result = False
        break

# 출력
if result == False:
    print("NO")
else:
    for i in answer:
        print(i)