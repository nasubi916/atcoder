# Past ABCs
import re

spritText = list(re.split("(...)", input())[1::2])
spritText[1] = int(spritText[1])

if spritText[1] == 316:
    print("No")
elif spritText[1] >= 350:
    print("No")
elif spritText[1] == 000:
    print("No")
else:
    print("Yes")
