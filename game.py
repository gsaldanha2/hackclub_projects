import pyglet
from player import Player
from ball import Ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class GameWindow(pyglet.window.Window):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.set_location(400, 100)
		self.player = Player()
		self.ball = Ball()

	def on_key_press(self, pressed, modifier):
		self.player.handle_key_pressed(pressed)

	def on_key_release(self, released, modifier):
		self.player.handle_key_released(released)

	def on_draw(self):
		self.clear()
		pyglet.graphics.draw(4, pyglet.gl.GL_POLYGON, ('v2f', (
			self.player.left, self.player.top,
			self.player.left, self.player.bottom,
			self.player.right, self.player.bottom,
			self.player.right, self.player.top
		)))
		self.ball.sprite.draw()

	def update(self, dt):
		self.player.update(dt)
		self.ball.update(self.player, dt)

if __name__ == '__main__': 
	game_window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
	pyglet.clock.schedule_interval(game_window.update, 1 / 60.0)
	pyglet.app.run()