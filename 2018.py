# 백준 2018번
n = int(input())

a = []
start_index = 0
end_index = 0
cnt = 0
sum_ = 0

for i in range(1, n+1):
    a.append(i)

while start_index < n:

    sum_ += a[end_index]
    end_index += 1
    if sum_ >= n:
        if sum_ == n:
            cnt += 1

        start_index += 1
        sum_ = 0
        end_index = start_index


print(cnt)