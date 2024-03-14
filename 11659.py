# 백준 온라인 저지 11659번
# 구간합 구하기

n, m = map(int, input().split())    # 수의 개수, 합을 구해야 하는 횟수
number_list = list(map(int, input().split()))   # n 개의 수
number_list = number_list[:n]

cnt = 0     # 질의 개수 카운트


sum_list = [0] # 구간합 배열
tmp = 0
result = []

# 합 배열 sum_list
for x in number_list:
    tmp += x
    sum_list.append(tmp)

while cnt < m:
    i, j = map(int, input().split())    # 구간
    result.append(sum_list[j] - sum_list[i-1])
    cnt += 1

print("============ 예제 출력 ============")

# 출력
for x in result:
    print(x)
