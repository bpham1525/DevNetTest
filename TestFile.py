class TestClassA:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

    def testfuncA(self):
        d = self.a
        e = self.b
        return d + e


class TestClassB(TestClassA):
    def __init__(self):
        TestClassA.__init__(self)
        self.d = 4
        self.c = 5

    def testfuncB(self):
        return self.d + self.c

    def testfuncC(self):
        return self.d + self.c


if __name__ == '__main__':
    print('Hello World')

    ta = TestClassA()
    tb = TestClassB()

    print(ta.testfuncA())
    print(tb.testfuncC())
