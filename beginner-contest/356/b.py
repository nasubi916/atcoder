inputs = input().split()

n = int(inputs[0])
m = int(inputs[1])

goals = list(map(int, input().split()))

for i in range(n):
    food = list(map(int, input().split()))
    for j in range(m):
        goals[j] = goals[j] - food[j]

if(max(goals) <= 0):
    print("Yes")
else:
    print("No")
