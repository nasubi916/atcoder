inputs = input().split()

n = int(inputs[0])

start = int(inputs[1])
end = int(inputs[2])

numbers = list()
for i in range(n):
    numbers.append(i + 1)
    if start <= i + 1 <= end:
        diff = i + 1 - start
        numbers.pop()
        numbers.append(end - diff)


print(" ".join(map(str, numbers)))
