class Area:
    @staticmethod
    def square(side ):
        return (side * side) if side > 0 else 0

    @staticmethod
    def rectangle(length, breadth):
        return length * breadth

    @staticmethod
    def triangle(breadth, height):
        return (breadth * height) / 2

    @staticmethod
    def circle(radius):
        return 3.14 * (radius * radius)
