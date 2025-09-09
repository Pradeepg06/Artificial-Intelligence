import random

class Environment:
    def __init__(self):
        # Two rooms: A and B
        self.locations = {"A": random.choice(["Clean", "Dirty"]),
                          "B": random.choice(["Clean", "Dirty"])}
        self.agent_location = random.choice(["A", "B"])

    def status(self, location):
        return self.locations[location]

    def clean(self, location):
        self.locations[location] = "Clean"

    def move(self, location):
        self.agent_location = location

    def is_done(self):
        return all(state == "Clean" for state in self.locations.values())


class ReflexVacuumAgent:
    def __init__(self):
        pass

    def act(self, env):
        location = env.agent_location
        status = env.status(location)

        if status == "Dirty":
            print(f"Location {location} is Dirty. Cleaning...")
            env.clean(location)
        else:
            # Move to the other room
            new_location = "B" if location == "A" else "A"
            print(f"Location {location} is Clean. Moving to {new_location}.")
            env.move(new_location)


# --- Simulation ---
env = Environment()
agent = ReflexVacuumAgent()

print("Initial Environment:", env.locations, "Agent at:", env.agent_location)

steps = 0
while not env.is_done() and steps < 10:
    agent.act(env)
    print("Environment:", env.locations, "Agent at:", env.agent_location)
    steps += 1

print("\nFinal Environment:", env.locations)
