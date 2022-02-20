from Person import Person


class Student(Person):
    def __init__(self, name, age, sid):
        super(Student, self).__init__(name, age)
        self.sid = sid

    # overwrite
    def print_func(self):
        print("My name is " + self.name + ", and I am student, my id is " + str(self.sid))

 
if __name__ == "__main__":
    s1 = Student("Zhang", 22, 1234)
    # call parent func
    s1.print_name()
    # call overwritten func
    s1.print_func()

    s1.print_private()
    #s1.print_log()
