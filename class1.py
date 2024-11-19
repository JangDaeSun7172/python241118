class Person:
    def __init__(self):
        self.name = 'default name'
    def print(self):
        print('my name is {0}'.format(self.name))

# Instance 생성
p1 = Person()
p2 = Person()
# 메스드 호출
p1.name = '전우치'
p1.print()
p2.print()