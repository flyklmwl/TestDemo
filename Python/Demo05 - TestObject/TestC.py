class Test:
    __type = 1
    bar = 1

    def __init__(self, arr1):
        self.arr = arr1
        self.__type = arr1

    def print_item(self):
        print(self.__type)


if __name__ == '__main__':
    test1 = Test("abc")
    test1.print_item()

    test2 = Test("123")
    print(test2.arr)

    classname = "TestB"
    test3 = getattr(__import__(classname), classname)("456")
    test3.showname()

    print(getattr(test2, 'bar'))
