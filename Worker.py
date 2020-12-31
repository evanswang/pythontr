from Person import Person


class Worker(Person):
    def __init__(self, *args, **kwargs):
        super(Worker, self).__init__(args[0], args[1])
        self.wid = args[2]
        if 'gender' in kwargs:
            self.gender = kwargs['gender']
        else:
            self.gender = 'secret'

    # overwrite
    def print_func(self):
        print("My name is " + self.name + ", and I am a " + self.gender + " worker, my wid is " + str(self.wid))


if __name__ == "__main__":
    w1 = Worker("Zhang", 22, 1234)
    # call parent func
    w1.print_name()
    # call overwritten func
    w1.print_func()
    w1.print_private()
