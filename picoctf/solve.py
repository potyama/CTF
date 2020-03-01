f = open("cattos.jpg", "rb").read()
g = open("kitters.jpg", "rb").read()

ans = ""

for i in range(len(f)):
    if f[i] != g[i]:
        ans += chr(f[i])

print(ans)
