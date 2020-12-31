class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__y = 3

    def print_func(self):
        print("Hello my name is " + self.name)

    def print_name(self):
        print("My name is " + self.name)

    def change_name(self, name):
        self.name = name

    def print_private(self):
        print('print private var: ' + str(self.__y))

    def change_private(self, y):
        self.__y = y


if __name__ == "__main__":
    p1 = Person('Wang', 12)
    # p1.name = 'Li'
    p1.print_name()
    p1.change_name('Zhang')
    p1.change_private(5)
    p1.print_private()
    p1.y = 2
    print(p1.name)
    # print(p1.__y)
    p2 = p1

    i = 1
    j = i
    j = 2
    print(i)
    print(j)
    p2.name = 'Li'
    p1.print_name()