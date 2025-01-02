def broadcast_message(sender, agents, message):
  for agent in agents:
      if agent != sender:
          sender.communicate(message, agent)