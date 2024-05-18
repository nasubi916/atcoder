people = int(input())

users = [[0 for j in range(2)] for i in range(people)]
sumNum = 0
for i in range(people):
    temp = input().split()
    for j in range(2):
        users[i][j] = temp[j]
        if j == 1:
            users[i][j] = int(users[i][j])
            sumNum += users[i][j]

users.sort()
winner = sumNum % people
print(users[winner][0])
