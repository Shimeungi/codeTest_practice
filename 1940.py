# 백준 1940번

n = int(input())
m = int(input())
num_arr = list(map(int, input().split()))
num_arr = sorted(num_arr)

start_index = 0
end_index = n-1
result = 0
cnt = 0
while start_index < end_index:
    result = num_arr[start_index] + num_arr[end_index]

    if result < m:
        start_index += 1
    elif result == m:
        cnt += 1
        start_index += 1
        end_index -= 1
    else:   # result > m
        end_index -= 1

print(cnt)


