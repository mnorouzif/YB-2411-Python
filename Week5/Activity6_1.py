class Student:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected
        self.__grade = 'A'     # private

    def get_grade(self):
        return self.__grade
    
    def get_updated_ stu(self):
         age = self._age+2
         return age

    

if __name__ == "__main__":
    s = Student('Ali', 20)
    print(" \n updated age:", s.get_stu)
    print(s.name)         # accessible
    print(s._age)         # discouraged
    print(s.get_grade())  # correct way
