f = open('demo.txt', 'wt', encoding='utf-8')
f.write('첫번째\n두번째\n세번째\n')
f.close()

f = open('demo.txt', 'rt', encoding='utf-8')
result = f.read()
print(result)
f.close()

f = open('demo.txt', 'rb')
result = f.read()
print(result)
f.close()

strA = 'python  is very powerful'
strB = '파이썬은 강력해'
print(len(strA))
print(len(strB))
print(strA.capitalize())
print('MBC2580'.isalnum())
print('2589'.isdecimal())

data = '<<< spam and ham >>>'
result = data.strip('<> ')
print(data)
print(result)

# 정규표현식
import re

result = re.search('[0-9]*th', '35th')
print(result)
print(result.group())

result = re.search('apple', 'this is apple')
print(result.group())

result = re.search('\d{4}', '올해는 2024년입니다.')
print(result)
print(result.group())