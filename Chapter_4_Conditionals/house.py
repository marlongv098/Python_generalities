from gasp import *          # import everything from the gasp library


def draw_house():
	begin_graphics()            # open the graphics canvas

	Box((20, 20), 100, 100)     # the house
	Box((55, 20), 30, 50)       # the door
	Box((40, 80), 20, 20)       # the left window
	Box((80, 80), 20, 20)       # the right window
	Line((20, 120), (70, 160))  # the left roof
	Line((70, 160), (120, 120)) # the right roof

	update_when('key_pressed')  # keep the canvas open until a key is pressed
	end_graphics()              # close the canvas (which would happen
                            # anyway, since the script ends here, but it
                            # is better to be explicit).

draw_house()
