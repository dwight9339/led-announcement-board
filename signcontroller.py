import time
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/lib/rpi-rgb-led-matrix/'))
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

class SignController(object):
	def __init__(self):
		options = RGBMatrixOptions()
		options.cols = 64
		self.matrix = RGBMatrix(options=options)
	
	# Writes message that scrolls from right to left
	def scrollRL(self, text, fontName, color, speed, repeat):
		offscreen_canvas = self.matrix.CreateFrameCanvas()
		font = graphics.Font()
		font.LoadFont("/lib/rpi-rgb-led-matrix/fonts/" + fontName + ".bdf")
		textColor = graphics.Color(*color)
		pos = offscreen_canvas.width
		textOffset = offscreen_canvas.height / 2 + font.height / 4
		l = graphics.DrawText(offscreen_canvas, font, pos, textOffset,textColor, text)
		
		for i in range(repeat):
			while pos + l > 0:
				offscreen_canvas.Clear()
				l = graphics.DrawText(offscreen_canvas, font, pos, textOffset, textColor, text)
				pos -= 1
				time.sleep(1/speed)
				offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
			pos = offscreen_canvas.width
			
		self.reset()
			
	# Message scrolls in from top
	def flyInTop(self, text, fontName, color, speed, hold_time):
		offscreen_canvas = self.matrix.CreateFrameCanvas()
		font = graphics.Font()
		font.LoadFont("/lib/rpi-rgb-led-matrix/fonts/" + fontName + ".bdf")
		textColor = graphics.Color(*color)
		pos = 0
		l = graphics.DrawText(offscreen_canvas, font, 0, pos, textColor, text)
		
		while pos < offscreen_canvas.height / 2 + font.height / 2:
			offscreen_canvas.Clear()
			l = graphics.DrawText(offscreen_canvas, font, 0, pos, textColor, text)
			pos += 1
			time.sleep(0.1)
			offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
			
		time.sleep(hold_time)
		self.reset()
		
			
	# Message scrolls in from bottom
	def flyInBottom(self, text, fontName, color, speed, hold_time):
		offscreen_canvas = self.matrix.CreateFrameCanvas()
		font = graphics.Font()
		font.LoadFont("/lib/rpi-rgb-led-matrix/fonts/" + fontName + ".bdf")
		textColor = graphics.Color(*color)
		pos = offscreen_canvas.height
		l = graphics.DrawText(offscreen_canvas, font, 0, pos, textColor, text)
		
		while pos > offscreen_canvas.height / 2 + font.height / 2:
			offscreen_canvas.Clear()
			l = graphics.DrawText(offscreen_canvas, font, 0, pos, textColor, text)
			pos -= 1
			time.sleep(0.1)
			offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
			
		time.sleep(hold_time)
		self.reset()
			
	def reset(self):
		self.matrix.Clear()
