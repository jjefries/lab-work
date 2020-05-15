class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def dist_between_two_points(self, other):
        slope_1 = self._x - other._x
        slope_2 = self._y - other._y
        return (slope_1 ** 2 + slope_2 ** 2) ** 0.5

p1=Point(5,6)
p2=Point(6,7)
print(p1.dist_between_two_points(p2))
