from pyglet.window import key

SPEED = 700

class Player:

	def __init__(self):
		self.x = 100
		self.velx = 0
		self.width = 100
		self.height = 15
		self._update_bounds()

	def _update_bounds(self):
		self.top = self.height
		self.left = self.x - self.width / 2
		self.right = self.x + self.width / 2
		self.bottom = 0

	def update(self, dt):
		self.x += self.velx * dt
		self._update_bounds()

	def handle_key_pressed(self, pressed):
		if pressed == key.RIGHT:
			self.velx = SPEED
		elif pressed == key.LEFT:
			self.velx = -SPEED

	def handle_key_released(self, released):
		if released == key.RIGHT or released == key.LEFT:
			self.velx = 0
