import time
import random

class Skill:
    def __init__(self, name, base_cost, base_effectiveness):
        self.name = name
        self.base_cost = base_cost
        self.base_effectiveness = base_effectiveness
        self.executions = 0
        self.total_utility = 0
        self.current_cost_multiplier = 1.0
        self.current_effectiveness_multiplier = 1.0

    def execute(self):
        # Simulate execution and calculate utility
        self.executions += 1
        execution_cost = self.base_cost * self.current_cost_multiplier * random.uniform(0.8, 1.2)
        execution_effectiveness = self.base_effectiveness * self.current_effectiveness_multiplier * random.uniform(0.8, 1.2)
        utility = execution_effectiveness - execution_cost
        self.total_utility += utility
        print(f"  Executing '{self.name}': Cost={execution_cost:.2f}, Effectiveness={execution_effectiveness:.2f}, Utility={utility:.2f}")
        return utility

    def measure_and_optimize(self):
        # Simple optimization: if utility is low, try to reduce cost or increase effectiveness
        if self.executions > 0:
            average_utility = self.total_utility / self.executions
            print(f"  Optimizing '{self.name}': Avg Utility={average_utility:.2f}")
            if average_utility < 10: # Threshold for optimization
                if random.random() < 0.5: # Chance to adjust cost
                    self.current_cost_multiplier *= random.uniform(0.9, 0.99)
                    print(f"    Adjusted cost multiplier to {self.current_cost_multiplier:.3f}")
                else: # Chance to adjust effectiveness
                    self.current_effectiveness_multiplier *= random.uniform(1.01, 1.1)
                    print(f"    Adjusted effectiveness multiplier to {self.current_effectiveness_multiplier:.3f}")
            elif average_utility > 50: # If performing very well, can afford to be more effective
                self.current_effectiveness_multiplier *= random.uniform(1.0, 1.05)
                print(f"    Increased effectiveness multiplier to {self.current_effectiveness_multiplier:.3f}")

class Agent:
    def __init__(self):
        self.skills = {
            "search": Skill("search", 5, 15),
            "analyze": Skill("analyze", 10, 25),
            "report": Skill("report", 8, 20)
        }
        self.current_task = None

    def set_task(self, task_name):
        self.current_task = task_name
        print(f"Agent: New task assigned - {task_name}")

    def choose_skill(self):
        # Simple skill selection based on task, could be more sophisticated
        if self.current_task == "information_gathering":
            return random.choice([self.skills["search"], self.skills["analyze"]])
        elif self.current_task == "reporting":
            return self.skills["report"]
        else:
            return random.choice(list(self.skills.values()))

    def run_cycle(self):
        if not self.current_task:
            print("Agent: No task assigned.")
            return

        print(f"Agent: Performing task '{self.current_task}'...")
        chosen_skill = self.choose_skill()
        print(f"Agent: Choosing skill '{chosen_skill.name}'...")
        
        # Execute the chosen skill
        chosen_skill.execute()
        
        # Agent-level optimization: Measure and optimize all skills
        print("Agent: Measuring and optimizing skills...")
        for skill in self.skills.values():
            skill.measure_and_optimize()
        print("---\n")

# --- Simulation ---
if __name__ == "__main__":
    agent = Agent()
    agent.set_task("information_gathering")

    for _ in range(5):
        agent.run_cycle()
        time.sleep(0.5) # Simulate time passing

    agent.set_task("reporting")
    for _ in range(3):
        agent.run_cycle()
        time.sleep(0.5)

    print("Simulation finished.")
