from collections import deque

N = int(input()) # 카드의 개수
queue = deque()

for i in range(1, N+1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft() # 맨 위 카드 버림
    queue.append(queue.popleft()) # 맨 위 카드 가장 밑으로 이동
    
print(queue[0])