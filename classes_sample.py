# !/usr/bin/env python3


class Dinosaur:

	def __init__(self, name: str, age: int) -> None:
		self.name = name
		self.age = age
		self.hunger = 0
		self.thirst = 0
		self.tiredness = 0
		self.health = 10


	def check_health(self) -> str:
		"""Check health of dinosaur and return it. If it is low, caution player.
		If it is 0 or less, raise warning"""
		if self.health <= 0:
			raise Warning(f'Your dinosaur {self.name} died! :(')
		elif self.health <= 5:
			return 'Your health is low! Eat, drink and sleep more!'
		else:
			return f"Your current health is {self.health}"

	def nourish(self, amount: int, t='food') -> str:
		if t == 'food':
			self.hunger -= amount
			self.health += 2
		elif t == 'drink':
			self.thirst -= amount
			self.health += 2
		else:
			print(f'Invalid type "{t}". Please choose between "food" and "drink".')
		self.check_health()
		return 'Buuurp'

	def sleep(self, time: int) -> None:
		self.tiredness -= time
		self.health += 5
		self.hunger += 5
		print('Snooore')
		self.check_health()

	def roar(self) -> None:
		pass

	def mate(self) -> None:
		print('Oi, mate!')
		self.check_health()

	def fight(self) -> None:
		self.health -= 10
		self.hunger += 10
		self.check_health()


class Brachiosaurus(Dinosaur):
	food = ['plants', 'water']

	def __init(self, name, age):
		super().__init__(name, age)

	@classmethod
	def check_food(cls, given: str) -> None:
		return given in cls.food

	def nourish(self, amount: int, t='water') -> str:
		if self.check_food(t):
			if t == 'plants':
				self.hunger -= amount
				self.health += 2
			elif t == 'water':
				self.thirst -= amount
				self.health += 2
			else:
				print(f'Invalid type "{t}". Please choose between "food" and "drink".')
			return 'Buuurp'
		else:
			print('Only eats plants and water!')
		self.check_health()

	@staticmethod 
	def roar() -> None:
		print('Raaaaa')


class Velociraptor(Dinosaur):
	food = ['meat', 'water']

	def __init(self, name, age, color):
		super().__init__(name, age)
		self.color = color

	@classmethod
	def check_food(cls, given: str) -> None:
		return given in cls.food

	def nourish(self, amount, t='water') -> str:
		if self.check_food(t):
			if t == 'meat':
				self.hunger -= amount
				self.health += 2
			elif t == 'water':
				self.thirst -= amount
				self.health += 2
			else:
				print(f'Invalid type "{t}". Please choose between "food" and "drink".')
			return 'Buuurp'
		else:
			print('Only eats meat and water!')
		self.check_health()

	@staticmethod 
	def roar() -> None:
		print('Riiiii')


if __name__ == '__main__':
	dino = Brachiosaurus('Sauri', 4)
	dino.mate()
	dino.roar()
	dino.fight()
