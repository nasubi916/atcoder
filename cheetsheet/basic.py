# Description: Pythonの基本的な構文をまとめたファイルです。
text:str = "Hello, World!"

#strをlistに変換
place:list[str] = list(text)

#listをstrに変換
strCreateCode = "".join(place)
commaSeparated = ",".join(place)

#listに要素を追加
place.append("x")

#listの要素を削除
del place[-1]

#listの要素を変更
place[1] = "x"

#listの長さを指定
array:list[int] = [0] * 26

#文字コードを取得
print(ord("a")) # 97

