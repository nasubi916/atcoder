dish = list(input())

rice = 0
miso = 0
for i in range(len(dish)):
    if dish[i] == 'R':
        rice =i
    if dish[i] == 'M':
        miso = i

if rice < miso:
    print("Yes")
else:
    print("No")