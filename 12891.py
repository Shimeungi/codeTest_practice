# 백준 12891번

def add(c):
    global myData, checkList, check_cnt

    if c == 'A':
        myData[0] += 1
        if myData[0] == checkList[0]:
            check_cnt += 1
    elif c == 'C':
        myData[1] += 1
        if myData[1] == checkList[1]:
            check_cnt += 1
    elif c == 'G':
        myData[2] += 1
        if myData[2] == checkList[2]:
            check_cnt += 1
    elif c == 'T':
        myData[3] += 1
        if myData[3] == checkList[3]:
            check_cnt += 1


def remove(c):
    global myData, checkList, check_cnt

    if c == 'A':
        if myData[0] == checkList[0]:
            check_cnt -= 1
        myData[0] -= 1

    elif c == 'C':
        if myData[1] == checkList[1]:
            check_cnt -= 1
        myData[1] -= 1

    elif c == 'G':
        if myData[2] == checkList[2]:
            check_cnt -= 1
        myData[2] -= 1

    elif c == 'T':
        if myData[3] == checkList[3]:
            check_cnt -= 1
        myData[3] -= 1


S, P = map(int, input().split())
S_arr = list(input())
checkList = list(map(int, input().split())) # A, C, G, T 최소 개수

myData = [0] * 4
check_cnt = 0
result = 0

for i in checkList:
    if i == 0:
        check_cnt += 1


for i in range(P):
    add(S_arr[i])

if check_cnt == 4:
    result += 1

for i in range(P, S):
    j = i - P # 시작점 옮기기
    add(S_arr[i])
    remove(S_arr[j])

    if check_cnt == 4:
        result += 1

print(result)



