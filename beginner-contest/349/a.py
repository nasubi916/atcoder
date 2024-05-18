# ゼロサム問題

playerNum = int(input())
eachPlayerScore: list[int] = list(map(int, input().split()))

totalScore = 0

for i in range(0, playerNum - 1, 1):
    totalScore += eachPlayerScore[i]

print(totalScore * -1)
