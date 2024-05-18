# Commencement

text: list[str] = input().split()

alphabetCount =[0] * 26

print(ord("a")) # 97

for c in text:
  # cの値はループごとに変化するので､それを利用してアルファベットの出現回数をカウントする
  alphabetCount[ord(c) - ord("a")] += 1

cnt2 = [0] * 101
for c in alphabetCount:
  if c > 0:
      cnt2[c] += 1

if all(c in (0, 2) for c in cnt2):
  print("Yes")
else:
  print("No")