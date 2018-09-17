from pyglet.window import key
import pyglet
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

SPEED = 500

class Ball:

	def __init__(self):
		self.x = 100
		self.y = 100

		self.velx = SPEED
		self.vely = SPEED
		self.radius = 20

		self.sprite = pyglet.sprite.Sprite(pyglet.image.load("resources/ball.png"), x=self.x, y=self.y)
		self.sprite.scale = self.radius * 2 / self.sprite.height


	def update(self, player, dt):
		self.x += self.velx * dt
		self.y += self.vely * dt
		self._bounce(player)

		self.sprite.x = self.x - self.radius
		self.sprite.y = self.y - self.radius

	def _bounce(self, player):
		if (self.x - self.radius <= 0):
			self.velx = -self.velx
			self.x = 0 + self.radius
		elif(self.x + self.radius >= SCREEN_WIDTH):
			self.velx = -self.velx
			self.x = SCREEN_WIDTH - self.radius
		elif self.y + self.radius >= SCREEN_HEIGHT:
			self.vely = -self.vely
			self.y = SCREEN_HEIGHT - self.radius
		elif self.y - self.radius <= 0:
			self.x = 500
			self.y = 500

		if (player.left <= self.x + self.radius) and (player.right >= self.x - self.radius) and (player.top >= self.y - self.radius):
			self.vely = -self.vely


