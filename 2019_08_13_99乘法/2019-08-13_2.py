x={
	"a":10,
	"b":"abc",
}
print(x)

x["c"] = "Hello"
print(x)

#del x["c"]
#print(x)

print(list(x.keys()))
print(list(x.values()))
