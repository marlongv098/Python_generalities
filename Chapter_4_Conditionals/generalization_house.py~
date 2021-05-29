from gasp import *          # import everything from the gasp library


def draw_house(x,y):
	begin_graphics()            # open the graphics canvas

	Box((x, y), x*5, y*5)     # the house
	Box(((x*3)-5, y), (x*2)+10, (y*3)-10)       # the door
	Box((x*2, y*4), x, y)       # the left window
	Box((x*4, y*4), x, y)       # the right window
	Line((x, y*6), ((x*3)+10, y*8))  # the left roof
	Line(((x*3)+10, y*8), (x*6, y*6)) # the right roof

	update_when('key_pressed')  # keep the canvas open until a key is pressed
	end_graphics()              # close the canvas (which would happen
                            # anyway, since the script ends here, but it
                            # is better to be explicit).
cat= input ("write x ")
bet= input ("write y ")
draw_house(cat,bet)		# THIS PROGRAM IS NOT FINISHED. I HAVE TO THING ON HOW MAY I A BETTER GENERALIZATION? 

