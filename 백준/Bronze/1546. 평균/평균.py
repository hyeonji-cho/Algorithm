N = int(input()) # 과목 개수
num_list = list(map(int,input().split(' '))) # N개의 시험 성적 저장

# 최댓값
M = max(num_list)

# 시험 성적 평균 
print((sum(num_list)/M * 100)/N)