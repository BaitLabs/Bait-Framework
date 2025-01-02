import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from baitframework.core import Agent
from baitframework.modules.movement import flocking

# Create 5 agents
agents = [Agent(agent_id=i) for i in range(5)]

# Move agents
flocking(agents)

# Print agent positions
for agent in agents:
    print(f"Agent {agent.agent_id} is at {agent.position}")