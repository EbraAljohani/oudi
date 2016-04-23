def compare(key, image):
	if key == image:
		True
	else:
		False

def generateText(text):
	head = text.Label(str(text),
					font_name='Georgia',
					font_size=24,
					x=WIDTH*0.1, y=HEIGHT*0.9)