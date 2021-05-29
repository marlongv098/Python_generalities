from gasp import *

begin_graphics()

Circle((200, 200), 60)
Line((100, 400), (580, 200))
Box((400, 350), 120, 100)

update_when('key_pressed')
end_graphics()
