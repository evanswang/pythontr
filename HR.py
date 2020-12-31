from Worker import Worker


class HR(Worker):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.salary = args[3]
        if 'religion' in kwargs:
            self.religion = kwargs['religion']
        else:
            self.religion = 'secret'

    # overwrite
    def print_func(self):
        print("My name is " + self.name + ", and I am a " + self.gender + " HR worker, my wid is " + str(self.wid))
        print("My salary is " + str(self.salary))
        print("My religion is " + self.religion)


if __name__ == "__main__":
    h1 = HR("Zhang", 22, 1234, 40000, gender='male', religion='buddist')
    # call parent func
    h1.print_name()
    # call overwritten func
    h1.print_func()
    h1.print_private()
