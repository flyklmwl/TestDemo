from TestClass import TestC


def test():
    for i in range(10):
        # print(i)
        yield i


class TestA(object):
    def __init__(self, name, sex, age, **kwargs):
        """
            定义成员变量
        """
    __v5 = "v5 value"
    v5 = "basis v5 value"

    def get(self, **kwargs):
        return self.client.get(**kwargs)

    def put(self, **kwargs):
        return self.client.put(**kwargs)

    def pop(self, **kwargs):
        return self.client.pop(**kwargs)


if __name__ == '__main__':
    student = TestA("xiaoc", "nan", "18")
    print(student.v5)
    print(student)

