import csv
from collections import Counter

def load_simulations(filepath="outputs/simulation_results.csv"):
    with open(filepath, "r") as file:
        return list(csv.DictReader(file))

def analyze_results(results):
    counts = Counter((row["coin"], row["box"]) for row in results)
    total_gold = sum(count for (coin, _), count in counts.items() if coin == "Gold")
    prob_gold_given_gold = counts[("Gold", "A")] / total_gold if total_gold else 0
    return {
        "total_gold": total_gold,
        "prob_gold_given_gold": prob_gold_given_gold
    }

def save_analysis(analysis, filepath="outputs/analysis_summary.txt"):
    with open(filepath, "w") as file:
        for key, value in analysis.items():
            file.write(f"{key}: {value}\n")

if __name__ == "__main__":
    results = load_simulations()
    analysis = analyze_results(results)
    save_analysis(analysis)