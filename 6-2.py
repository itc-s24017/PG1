class Sample:
    def __init__(self):
        self.a = 1
        self._b = 1
        self.__c = 1
        self.__d_ = 1
        self.__e__ = 1

    def show_attribute(self):
        a = self.a
        b = self._b
        c = self.__c
        d = self.__d_
        e = self.__e__
        print("a: {}, b: {}, c: {}, d: {}, e: {}".format(a, b, c, d, e))

s = Sample()
s. show_attribute()

print(s.a)
print(s._b)

