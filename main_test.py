from test import Pointer

p=Pointer(20,20)
print(p.x)
print(p.y)
p.move_right()
print(p.x)
p.move_left()
p.move_left()
print(p.x)