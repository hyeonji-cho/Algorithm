N = int(input()) # 숫자의 개수
num_list = list(map(int,input())) # N개의 숫자 저장

# N개의 숫자 합
total_sum = 0
for num in num_list:
    total_sum += num
print(total_sum)