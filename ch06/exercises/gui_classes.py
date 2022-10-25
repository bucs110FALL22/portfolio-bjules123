class Screen:
 def __init__(self):
  self.score = 0
  self.amount = 1 
  self.is_red = True 

class Game:
 def __init__(self):
  self.pipes_are_green = True
  self.bricks = 100
  self.enemies = 10 

class Mario:
 def __init__(self):
  self.time_untouched = 60
  self.friends = 1 
  self.obstacles = 25 