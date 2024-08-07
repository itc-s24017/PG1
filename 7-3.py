import sys

class MyValueLimitError(Exception):
    def __init__(self, x1, x2, limit_num):
        self.x1 = x1
        self.x2 = x2
        self.limit_num = limit_num

    def __str__(self):
        return '値の範囲を超えてる{0} {1} {2} '.format(self.x1, self.x2, self.limit_num)

def multiplcation_limit(x1, x2, limit_num):
    try:
        x = x1 * x2
        if x > limit_num:
            raise MyValueLimitError(x1, x2, limit_num)
        raise x
    except MyValueLimitError as vle:
        print(vle)
        return limit_num
    except:
        print('Unexpected Error:', sys.exc_info())
        return None

limit_num = 10000
multiplcation_limit(100, 101, limit_num)
