def round_robin(agents, tasks):
  for i, task in enumerate(tasks):
      agents[i % len(agents)].task = task