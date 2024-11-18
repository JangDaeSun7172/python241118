#: function.py
def times(a,b):
    return a*b
result = times(5,6)
print(result)

def setValue(newV):
    x = newV
    print("내부:", x)
result = setValue(5)
print(result)

def intersect(p,q):
    result = []
    for x in p:
        if x in q and x not in result:
            result.append(x)
    return result

print(intersect("HAM","SPAM"))