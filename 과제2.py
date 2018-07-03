class man:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class coworkers(man):

    def __init__(self, name, age, gender, position):
        # super()내장함수 부모클래스를 가지고 있는 함수(변수)를 호출
        super().__init__(name, age, gender)
        self.position = position


man1 = coworkers("김다슬",25,"여","과장")

# print(man1.age)

print(man1.__dict__) # => 딕셔너리형식으로 파일 내용 보여줌
