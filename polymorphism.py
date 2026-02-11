#polymorphism - many forms a method can have
class Rectangle:
      def draw(self):
        print("Drawing a rectangle")

class Rhombus:
    def draw(self):
        print("Drawing a rhombus")

class Parallelogram:
    def draw(self):
        print("Drawing a parallelogram")

r = Rectangle()
r.draw()

rh = Rhombus()
rh.draw()

p = Parallelogram()
p.draw()
