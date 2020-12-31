from Person import Person
from LoggingHandler import LoggingHandler
import logging


class Student(Person):
    def __init__(self, name, age, sid):
        super(Student, self).__init__(name, age)
        self.sid = sid
        self.logger = LoggingHandler(self.__class__.__name__, logging.DEBUG)

    # overwrite
    def print_func(self):
        print("My name is " + self.name + ", and I am student, my id is " + str(self.sid))

    def print_log(self):
        self.logger.log.info("My sid is " + str(self.sid))
        self.logger.log.debug(self.name + " : " + str(self.age) + " : " + str(self.sid))


if __name__ == "__main__":
    s1 = Student("Zhang", 22, 1234)
    # call parent func
    s1.print_name()
    # call overwritten func
    s1.print_func()

    s1.print_private()
    #s1.print_log()