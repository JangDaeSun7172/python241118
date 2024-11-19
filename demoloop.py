value = 5
while value > 0:
    print(value)
    value -= 1

lst = [100, 'python', 3.14]
for itm in lst:
    print(itm, type(itm))

fru = {'apple':'red', 'kiwi':'green'}
for k,v in fru.items():
    print(k,v)

print(list(range(10)))
print(list(range(1,32)))

lst = list(range(1,11))
print(lst)
print([i**2 for i in lst if i>5])

tp = ('apple', 'kiwi')
print([len(i) for i in tp])

lst = [10,25,30]
itemL = filter(None, lst)
for item in itemL:
    print(item)

print('getBigger')
def getBiggerThan20(i):
    return i > 20
itemL = filter(getBiggerThan20, lst)
for item in itemL:
    print(item)

print('lambda')
itemL = filter(lambda i:i>20, lst)
for item in itemL:
    print(item)