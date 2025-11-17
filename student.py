class Student:
    def __init__(self,fnum=0,name="",avMark=0):
        self.fnum=fnum
        self.name=name
        self.avMark=avMark
    def __str__(self):
        return f"({self.fnum},{self.name},{self.avMark})"
class Group:
    def __init__(self,group=None):
        if self.group==None:
            self.group=[]
        else :
            self.group=group
    def addStudent(self,student):
        self.group.append(student)
    def delStudent(self,student):
        if student in self.group:
            self.group.remove(student)
    def delStudentbyFnum(self,fnum):
        for i in range(0,len(self.group)):
            student=self.group[i]
            if student.fnum ==fnum:
                self.group.remove(student)
        return
