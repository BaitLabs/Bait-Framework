class Agent:
  def __init__(self, agent_id, position=(0, 0)):
      self.agent_id = agent_id
      self.position = position

  def move(self, dx, dy):
      self.position = (self.position[0] + dx, self.position[1] + dy)

  def communicate(self, message, target):
      target.receive_message(message)

  def receive_message(self, message):
      print(f"Agent {self.agent_id} received message: {message}")