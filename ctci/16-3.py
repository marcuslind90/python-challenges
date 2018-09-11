class Point(object):
    def __init__(self, x, y, *args, **kwargs):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x}, {self.y}"


class Line(object):
    def __init__(self, start, end, *args, **kwargs):
            self.delta_y = end.y - start.y
            self.delta_x = end.x - start.x
            self.slope = (self.delta_y / self.delta_x) if self.delta_x != 0 else float("inf") # noqa
            self.y_intercept = end.y - self.slope * end.x


def intersect(start1, end1, start2, end2):
    """
    Given 2 lines represented by starting and ending points,
    calculate and return the intersect point.
    """
    # Swap points to make sure that they are in
    # a logical order from left -> right.
    if start1.x > end1.x:
        start1, end1 = end1, start1
    if start2.x > end2.x:
        start2, end2 = end2, start2
    if start1.x > start2.x:
        start1, start2 = start2, start1
        end1, end2 = end2, end1

    line1 = Line(start1, end1)
    line2 = Line(start2, end2)

    # If the angles are the same, they will only intersect if
    # they are on the same intercept and start2 is between start1 and end1.
    if line1.slope == line2.slope:
        if line1.y_intercept == line2.y_intercept and \
           is_between_points(start1, start2, end1):
            return start2
        return None

    x = (line2.y_intercept - line1.y_intercept) / (line1.slope - line2.slope)
    y = x * line1.slope + line1.y_intercept
    intersection = Point(x, y)

    if is_between_points(start1, intersection, end1) and \
       is_between_points(start2, intersection, end2):
        return intersection
    return None


def is_between(start, middle, end):
    if start > end:
        return end <= middle and middle <= start
    else:
        return start <= middle and middle <= end


def is_between_points(start, middle, end):
    return is_between(start.x, middle.x, end.x) and \
        is_between(start.y, middle.y, end.y)


point = intersect(Point(0, 0), Point(5, 5), Point(2, 5), Point(4, 0))
assert point is not None, "Intersection is wrong."
