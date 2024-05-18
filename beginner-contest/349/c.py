# Airport Code

place = list(input())
code = input()

createCode: list[str] = []

for i in range(0, place.__len__(), 2):
    if i > 6:
        del createCode[-1]
        createCode[-1] = "x"
        break
    else:
        createCode.append(place[i])

strCreateCode = "".join(createCode)
upperCode = strCreateCode.upper()

if upperCode == code:
    print("Yes")
else:
    print("No")

print(upperCode,code)