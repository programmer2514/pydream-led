pydream-led
===========

Python interface for talking to the Dream Cheeky 21x7 LED display (VendorId: 0x1d34 DeviceId: 0x0013)

I'm new to Python; as a result, there may be some strage approaches here. I'm
open to accepting pull requests to improve the code, such as:

* better modularity
* support for other LED signs
* reducing reliance on "magic numbers"

Basic use
---------

First, install using `python setup.py install`

Or, if you prefer using PyPI: `pip install pydream-led`

The package should auto-install `pyusb`, but you will need to install libusb (upon which pyusb depends) for things to work. libusb is available for most Linux distros via their package managers, and via Homebrew on OS X.

We create an instance of the `display` object and connect:

	import pydream

	sign = pydream.display()
	if not sign.connect():
		raise StandardError("Cannot connect to sign")

Then we set up a "frame" that we wish to display. We can do this using a combination of methods:

	sign.light_on(0,0)  # turn light in upper-right corner on
	sign.light_off(0,0) # the opposite
	
	# clear_state below the "background"; 0=off, 1=on
	sign.move_left(clear_state=0, count=1)   # move the frame left one
	sign.move_right(clear_state=0, count=1)  # move the frame right one
	sign.move_up(clear_state=0, count=1)     # up
	sign.move_down(clear_state=0, count=1)   # down

	sign.put_sprite(0,0,sprite)  # see Sprite section

	sign.clear()  # make sign black
	sign.clear(1) # make sign lit

We can also just specify the frame directly, like so:
	
	disp.current_frame = [
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
		]

This approach isn't generally encouraged, which is why no method is provided
to support it. `current_frame` must be a list of 7 "rows" with 21 "columns"
each. A 1 represents a lit LED, a 0 is an unlit LED.

By combining these methods, we set up the frame we want to see, then tell the
display to refresh:

	sign.refresh()

**NOTE:** this LED sign will only display for about 0.4 seconds for each 
refresh. To maintain an image, `refresh()` must be called at least that 
frequently.

Sprites
-------

To draw a shape on the screen without turning each light on individually,
you can define a sprite. This is a list of lists that forms the rows and
columns of lit and unlit LEDs which define a shape. Like so:

	eye = [
	    	[0,0,1,0,0],
		    [0,1,0,1,0],
		    [1,0,0,0,1],
		    [0,1,0,1,0],
		    [0,0,1,0,0]
		   ]

You can then put this sprite on the display using the `put_sprite` method.
Putting a sprite changes the area of the frame you put the sprite to, but
otherwise leaves the frame alone.

This method supports several modes of drawing.

	sign.put_sprite(0, 0, eye) # draw the eye at 0,0; replace what's there
	sign.put_sprite(0, 0, eye, mode='and') # bitwise AND the sprite with the frame at this location

Possible modes to specify are:

- `replace`: the default. Replace the area of the frame with the sprite
- `and`: bit-wise AND the sprite with the frame area's content
- `or` : as `and`, but using bitwise OR
- `xor`: as `and`, but using bitwise XOR
- `clear`: turn off all LEDs in the sprite area
- `fill` : turn on all LEDs in the sprite area
- `
