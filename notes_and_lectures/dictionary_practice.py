d = {
	"foo":"poo",
	"foo1":"poo1"
}

for k in d:
	print("{}\t{}".format(k,d[k])

foo = list(d.keys())
foo.sort()

for k in foo:
	print(k,d[k])



