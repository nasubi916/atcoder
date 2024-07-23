aaa = input().split()

s = aaa[0]
t = aaa[1]

for w in range(1, len(s)):
    for c in range(w):
        now = ""
        for i in range(c, len(s), w):
            now += s[i]
        if now == t:
            print("Yes")
            exit()

    # loop = int(len(aaa[1]))

    # textLen = int(len(aaa[0]) / loop)
    # answer = []

    # for i in range(loop):
    #     # if len(aaa[0]) <= len(aaa[1]):
    #     #     break
    #     # if len(aaa[1]) == 1:
    #     #     if not (len(aaa[0]) < 4):
    #     #         break
    #     splitText = aaa[0][i * textLen : (i + 1) * textLen]
    #     for j in range(len(splitText)):
    #         print(splitText[j])
    #         a = "".join(splitText[j])
    #         print(a)
    #     # answer.append()

    # if "".join(answer) == aaa[1]:
    #     print("Yes")
    # else:
    #     print("No")
