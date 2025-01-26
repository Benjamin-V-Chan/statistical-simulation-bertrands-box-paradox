import csv
import matplotlib.pyplot as plt

def load_analysis(filepath="outputs/analysis_summary.txt"):
    analysis = {}
    with open(filepath, "r") as file:
        for line in file:
            key, value = line.strip().split(": ")
            analysis[key] = float(value)
    return analysis

def visualize_results():
    analysis = load_analysis()
    labels = ["Gold Given Gold"]
    values = [analysis["prob_gold_given_gold"]]
    plt.bar(labels, values)
    plt.title("Probability of Gold Coin Given Gold")
    plt.savefig("outputs/visualizations/probability_chart.png")

if __name__ == "__main__":
    visualize_results()