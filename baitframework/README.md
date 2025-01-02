# Bait Framework

Bait Framework is a modular swarm intelligence framework designed for building and managing customizable AI agents.

## Features
- **Modular Design**: Easily customize agent behavior, communication protocols, and task allocation.
- **Beginner-Friendly**: Includes simple examples to help users get started.
- **Scalable**: Build complex swarm behaviors with minimal effort.

## Installation
The framework is under development and not yet available on PyPI. You can clone this repository to start using it:

```bash
git clone https://github.com/<your-username>/BaitFramework.git
from baitframework.core import Agent
from baitframework.modules.movement import flocking

# Create 5 agents
agents = [Agent(agent_id=i) for i in range(5)]

# Move agents
flocking(agents)

# Print agent positions
for agent in agents:
    print(f"Agent {agent.agent_id} is at {agent.position}")
    Examples

    We’ve included example scripts to help you get started. Check out the examples/ folder for more:
      •	Basic Swarm Example: Demonstrates how to create agents and apply basic movement logic.

    Contributing

    We welcome contributions! If you’d like to improve this framework, please:
      1.	Fork the repository.
      2.	Create a feature branch.
      3.	Submit a pull request with your changes.

    License

    This project is licensed under the MIT License. See the LICENSE file for details.