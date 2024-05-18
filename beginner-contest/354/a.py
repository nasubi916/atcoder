tall = 0
day = 0

takahashi = int(input())

while True:
    day += 1
    tall += pow(2, day - 1)
    if takahashi < tall:
        break

print(day)