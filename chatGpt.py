class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")

# 테스트 코드
def test():
    # 1. Person 클래스 테스트
    p1 = Person(1, "Alice")
    p1.printInfo()
    
    # 2. Person 클래스의 다른 객체
    p2 = Person(2, "Bob")
    p2.printInfo()
    
    # 3. Manager 클래스 테스트
    m1 = Manager(3, "Charlie", "Team Lead")
    m1.printInfo()
    
    # 4. Manager 클래스의 다른 객체
    m2 = Manager(4, "Dana", "Project Manager")
    m2.printInfo()
    
    # 5. Employee 클래스 테스트
    e1 = Employee(5, "Eve", "Python")
    e1.printInfo()
    
    # 6. Employee 클래스의 다른 객체
    e2 = Employee(6, "Frank", "Data Analysis")
    e2.printInfo()
    
    # 7. Manager와 Employee 상속 관계 확인
    assert isinstance(m1, Person), "Manager는 Person을 상속받아야 합니다."
    assert isinstance(e1, Person), "Employee는 Person을 상속받아야 합니다."
    
    # 8. Person 객체와 상속된 객체 비교
    assert not isinstance(p1, Manager), "Person은 Manager가 아닙니다."
    assert not isinstance(p1, Employee), "Person은 Employee가 아닙니다."
    
    # 9. 여러 객체 생성 및 정보 출력
    m3 = Manager(7, "Grace", "Director")
    e3 = Employee(8, "Hank", "Java")
    m3.printInfo()
    e3.printInfo()
    
    # 10. 다양한 객체를 리스트로 관리 및 출력
    people = [p1, p2, m1, m2, e1, e2, m3, e3]
    for person in people:
        person.printInfo()
        print("---")

# 테스트 실행
test()
