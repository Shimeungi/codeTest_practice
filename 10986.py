n, m = map(int, input().split()) # n : n개의 수 // m : 구간 나눌 숫자
n_list = list(map(int, input().split()))    # n 개의 수 list
s_list = []     # 구간 합 list

tmp = 0
cnt = 0 # 합이 m으로 떨어지는 쌍의 개수
cnt_list = [0] * m  # 크기 m 만큼의 나머지 배열

# 구간합 list
for i in n_list:
    tmp += i
    s_list.append(tmp)

# 구간합 % m
for i in range(n):
    s_list[i] = s_list[i] % m

    if s_list[i] == 0:
        cnt += 1

# 나머지 같은 합배열 cnt_list 에 카운트
for i in range(n):
    for j in range(m):
        if s_list[i] == j:
            cnt_list[j] += 1


for i in range(m):
    if cnt_list[i] > 1:
        cnt += (cnt_list[i] * (cnt_list[i] - 1) // 2)


print(cnt)