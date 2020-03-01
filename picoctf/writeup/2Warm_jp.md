# 2Warm - Points: 50
# 問題文
Can you convert the number 42 (base 10) to binary (base 2)? 

# Hint
Submit your answer in our competition's flag format. For example, if you answer was '11111', you would submit 'picoCTF{11111}' as the flag.

# 訳
42(10進数)をバイナリ(2進数)に変換できますか？

# 解法
頭のなかで変換すれば終わりです。

42(10) -> 101010(2)

一応、[変換サイト](https://hogehoge.tk/tool/number.html
)もありますので、そこで変換するもありです。

プログラムだとこんな感じです。

```Python
binary = format(42, 'b')

print(binary)
```
よって答えは101010なので{}の中に入れたら終わりです。
```
picoCTF{101010}
```
