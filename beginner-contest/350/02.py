# Dentist Aoki

aaa = list(map(int, input().split()))
bassi = list(map(int, input().split()))
tooth = [False] * aaa[0]



count = 0
for x in tooth:
    if not x:
        count += 1

print(count)
