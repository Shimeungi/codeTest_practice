n, m = map(int, input().split()) # 2차원 배열의 크기, 구간 합 질의의 수

a = [[0] * (n+1)]   # 입력받는 배열
b = [[0] * (n+1) for _ in range(n+1)]   # 합배열


for i in range(n):
    a_row = [0] + [int(x) for x in input().split()]
    a.append(a_row)

for i in range(1, n+1):
    for j in range(1, n+1):
        b[i][j] = b[i-1][j] + b[i][j-1] - b[i-1][j-1] + a[i][j]


for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = b[x2][y2] - b[x1-1][y2] - b[x2][y1-1] + b[x1-1][y1-1]
    print(result)


