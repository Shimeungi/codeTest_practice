
# change score function
def change_score(scores, m ): # list, max_score
    score_list = []
    for num in scores:
        score = num / m * 100
        score_list.append(score)

    return score_list

### main ###
n = int(input())
scores = list(map(int, input().split())) # 공백을 기준으로 int 형 자료형 입력
max_score = max(scores)
new_score = [] # 고친 점수
sum = 0
avg = 0
new_score = change_score(scores, max_score)

for num in new_score:
    sum += num

avg = sum / len(new_score)


print(avg)