
alpha = "abcdefghijklmnopqrstuvwxyz"

base = "isrveawhobpnutfg\260\001"
final = "giants"

res = list(map(str, "giants"))

for char in alpha:
	index = (ord(char) & 0xf)
	print(index, end=" ")
	print(base[index])
	if base[index] in final:
		print(final.index(base[index]), res)
		res[final.index(base[index])] = char

print("res: ", res)
