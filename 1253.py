# 백준 1253번
n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

start_idx = 0
end_idx = n-1
cnt = 0

for idx in range(n):
    target = n_list[idx]
    start_idx = 0
    end_idx = n - 1

    while start_idx < end_idx:
        result = n_list[start_idx] + n_list[end_idx]

        if result > target:
            end_idx -= 1
        elif result < target:
            start_idx += 1
        else:
            if start_idx != idx and end_idx != idx:
                cnt += 1
                break
            elif start_idx == idx:
                start_idx += 1
            elif end_idx == idx:
                end_idx -= 1

print(cnt)


