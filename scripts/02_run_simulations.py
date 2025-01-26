import csv
import random

def load_scenarios(filepath="outputs/scenarios.csv"):
    with open(filepath, "r") as file:
        return list(csv.DictReader(file))

def run_simulations(scenarios, num_simulations=10000):
    results = []
    for _ in range(num_simulations):
        choice = random.choice(scenarios)
        results.append({"box": choice["box"], "coin": choice["coin"]})
    return results

def save_simulations(results, filepath="outputs/simulation_results.csv"):
    with open(filepath, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["box", "coin"])
        writer.writeheader()
        writer.writerows(results)

if __name__ == "__main__":
    scenarios = load_scenarios()
    results = run_simulations(scenarios)
    save_simulations(results)