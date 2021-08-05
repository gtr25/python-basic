class StringExpression:
    def __init__(self, x):
        self.x = x

    def __truediv__(self, other):
        result = int(self.x) + 2 * (int(other.x))
        return result

