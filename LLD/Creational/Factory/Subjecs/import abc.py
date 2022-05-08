import abc
class Subject(abc.ABC):
    def __init__(self, exam_marks) -> None:
        self.__exam_marks = exam_marks
    
    @property
    def exam_marks(self):
        return self.__exam_marks
    
    @abc.abstractproperty
    def topics(self):
        pass


class Maths(Subject):
    def topics(self):
        return ["Trigonometry", "Algebra"]

class Chemistry(Subject):
    def topics(self):
        return ["Organic", "Inorganic"]

class Physics(Subject):
    def topics(self):
        return ["Newton, Einstine"]


class SubjectFactory:
    def get_subject(self, subject_name):
        if subject_name == "Maths":
            return Maths(200)
        elif subject_name == "Chemistry":
            return Chemistry(100)
        elif subject_name == "Physics":
            return Physics(100)

class One:
    def __init__(self) -> None:
        self.factory = SubjectFactory()
        self.subject1 = self.factory.get_subject("Maths")
        self.subject2 = self.factory.get_subject("Chemistry")

class Two:
    def __init__(self) -> None:
        self.factory = SubjectFactory()
        self.subject1 = self.factory.get_subject("Physics")
        self.subject2 = self.factory.get_subject("Chemistry")



one = One()
print(one.subject1.exam_marks)
print(one.subject1.topics())
Two()
# class One: 
#     def __init__(self) -> None:
#         self.subject1 = Maths(100)
#         self.subject2 = Chemistry(100)

# class 2 : Chemistry, Physics
# class 3 : Maths, Physics
# class 4 : Physics, Chemistry, Maths
