import abc
class Subject(abc.ABC):
    def __init__(self, exam_marks) -> None:
        self.__exam_marks = exam_marks
    
    @property
    def exam_marks(self):
        return self.__exam_marks


class Maths(Subject):
    def __init__(self, exam_marks, topics) -> None:
        super().__init__(exam_marks)
        self.__topics = topics

class Chemistry(Subject):
    def __init__(self, exam_marks, topics) -> None:
        super().__init__(exam_marks)
        self.__topics = topics

class Physics(Subject):
    def __init__(self, exam_marks, topics) -> None:
        super().__init__(exam_marks)
        self.__topics = topics

class UniversityAbstract(abc.ABC):
    def __init__(self) -> None:
        self.subject_factory = SubjectFactory()

    @abc.abstractproperty
    def physics(self):
        pass
    
    @abc.abstractproperty
    def maths(self):
        pass

    @abc.abstractproperty
    def chemistry(self):
        pass

class IIITBUniversityFactory(UniversityAbstract):
    def physics(self):
        physics = self.subject_factory.get_subject("Physics", ["Physics1", "Physics2"])
        return physics
    def maths(self):
        maths = self.subject_factory.get_subject("Maths", ["Maths1", "Maths2"])
        return maths
    def chemistry(self):
        chemistry = self.subject_factory.get_subject("Chemistry", ["Chemistry1", "Chemistry2"])
        return chemistry

class WalchandUniversityFactory(UniversityAbstract):
    def physics(self):
        physics = self.subject_factory.get_subject("Physics", ["Physics3", "Physics4"])
        return physics
    def maths(self):
        maths = self.subject_factory.get_subject("Maths", ["Maths3", "Maths4"])
        return maths
    def chemistry(self):
        chemistry = self.subject_factory.get_subject("Chemistry", ["Chemistry3", "Chemistry4"])
        return chemistry

class SubjectFactory:
    def get_subject(self, subject_name, topics):
        if subject_name == "Maths":
            return Maths(200, topics)
        elif subject_name == "Chemistry":
            return Chemistry(100, topics)
        elif subject_name == "Physics":
            return Physics(100, topics)



# class CourseOne:
#     def __init__(self) -> None:
#         self.factory = SubjectFactory()
#         self.subject1 = self.factory.get_subject("Maths")
#         self.subject2 = self.factory.get_subject("Chemistry")

# class CourseTwo:
#     def __init__(self) -> None:
#         self.factory = SubjectFactory()
#         self.subject1 = self.factory.get_subject("Physics")
#         self.subject2 = self.factory.get_subject("Chemistry")



# one = CourseOne()
# print(one.subject1.exam_marks)
# print(one.subject1.topics())
# Two()
# class One: 
#     def __init__(self) -> None:
#         self.subject1 = Maths(100)
#         self.subject2 = Chemistry(100)

# class 2 : Chemistry, Physics
# class 3 : Maths, Physics
# class 4 : Physics, Chemistry, Maths
