arr = []
N = int(input()) # 수의 개수

# 수 입력받기
for i in range(N):
    m = int(input())
    arr.append(m)

# 오름차순 정렬
arr.sort() 

# 정렬된 결과 출력 
for i in arr:
    print(i)
