deck = int(input())

cards = [[0 for j in range(2)] for i in range(deck)]
# cards[[attack,cost],...]
# trash if attack < かつ cost >

for i in range(deck):
    temp = input().split()
    for j in range(2):
        cards[i][j] = int(temp[j])

pickCards = []
for i in range(deck):
    for j in range(i + 1):
        if cards[i][0] > cards[j][0] and cards[i][1] < cards[j][1]:
            pickCards.append(i)
            break

print(len(pickCards))
print(",".join(pickCards))
