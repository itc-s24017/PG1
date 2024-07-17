def make_circle_area_func(pi = 3.14):
    '''関数'''
    def circle_area(radius):
        '''計算'''
        return radius * radius * pi
    return circle_area

circle_area_default = make_circle_area_func()

circle_area_precise = make_circle_area_func(pi = 3.1415926535)

type(circle_area_default), type(circle_area_precise)

print(circle_area_default(2))
print(circle_area_precise(2))
