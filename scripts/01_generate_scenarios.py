import random
import csv

def generate_scenarios():
    boxes = {
        "A": ["Gold", "Gold"],
        "B": ["Gold", "Silver"],
        "C": ["Silver", "Silver"]
    }
    scenarios = []
    for _ in range(10000):
        box = random.choice(list(boxes.keys()))
        coin = random.choice(boxes[box])
        scenarios.append({"box": box, "coin": coin})
    return scenarios

def save_scenarios(scenarios, filepath="outputs/scenarios.csv"):
    with open(filepath, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["box", "coin"])
        writer.writeheader()
        writer.writerows(scenarios)

if __name__ == "__main__":
    scenarios = generate_scenarios()
    save_scenarios(scenarios)