from sys import argv
if len(argv) < 3:
    print("two arguments, sil vous plait")
try:
    a = int(argv[1])
    b = int(argv[2])
    print("{} + {} = {}".format(a,b, a + b))
except:
    print("Use parseable ints bruv!")
    quit()