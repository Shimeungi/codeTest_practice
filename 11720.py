index = int(input())
numbers = list(input())
numbers = numbers[:index]
sum = 0
for n in numbers:
    sum += int(n)

print(sum)