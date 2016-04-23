from pyglet.window import Window
from pyglet.window import key
from pyglet import app 
from pyglet import text
from pyglet import clock
from pyglet import image
from pyglet import sprite
from pyglet import graphics
from pyglet import sprite
import random
import func

HEIGHT=480
WIDTH=640

window = Window(width=WIDTH, height=HEIGHT)

head = text.Label('Play the following note(s):',
					font_name='Georgia',
					font_size=24,
					x=WIDTH*0.1, y=HEIGHT*0.9)

correct = text.Label('Correct!',
						font_name='Georgia',
						font_size=36,
						x=WIDTH*0.5, y=HEIGHT*0.5)

wrong = text.Label('Try again',
						font_name='Georgia',
						font_size=15,
						x=WIDTH*0.2, y=HEIGHT*0.3)

rand = random.randint(1,6)

if rand == 1:
	note = 'c.png'
elif rand == 2:
	note = 'd.png'
elif rand == 3:
	note = 'e.png'
elif rand == 5:
	note = 'f.png'

answerBatch = graphics.Batch()
imageToPlay = image.load(note)



@window.event
def on_draw():
	window.clear()
	head.draw()
	imageToPlay.blit(WIDTH*0.15, HEIGHT*0.65)
	 #answerBatch.draw()

@window.event
def on_key_press(symbol, modifiers):
	if symbol == key.C:
		if 'c.png'== note:
			print 'A C was pressed'
			print 'Correct!'
		else:
			print 'Wrong!'
	if symbol == key.D:
		if 'd.png'== note:
			print 'A D was pressed'
			print 'Correct!'
		else:
			print 'Wrong!'
	if symbol == key.E:
		if 'e.png'==note:
			print 'A E was pressed'
			print 'Correct!'
		else:
			print 'Wrong!'
	if symbol == key.F:
		if 'f.png'==note:
			print 'A F was pressed'
			print 'Correct!'
		else:
			print 'Wrong!'



fSong = 500 
fPlay = 500

def pitchComp(fSong, fPlay):
	if abs(fSong - fPlay)  < 3:
		return True
	else:
		return False

print pitchComp(fSong, fPlay)

app.run()