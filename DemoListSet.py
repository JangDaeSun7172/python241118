# DemoListSet.py
colors = ["red"]
print(colors)
colors.append("blue")
print(colors)
colors.append("yellow")
print(colors)
colors.remove("blue")
print(colors)

#Set
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#Tuple
def calc(a,b):
    return a+b, a*b

print(calc(5,5))
args = (4,5)
print(calc(*args))
print("id: %s, name:%s" % ("Kim","김유신"))

#Dict
dic = {"a":1, "b":[1,2]}
print(dic)
dic["c"]=3
print(dic)
dics = dict(a=[1,2,3],b=["a","b"])
print(dics)
for item in dics.items():
    print(item)