name = "Georgii Kaigorodov"
name = list(name)

for i in range(1, len(name) * 2, 2):
    name.insert(i, "_")

name = list(map(ord, name))

print(max(name),min(name))