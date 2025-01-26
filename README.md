# statistical-simulation-bertrands-box-paradox

# Bertrand's Box Paradox Simulation

## Project Overview
This project simulates the Bertrand's Box Paradox, a classic probability puzzle that challenges intuitive reasoning. The paradox is as follows:

- There are three boxes:
  - Box A: Contains two gold coins.
  - Box B: Contains one gold coin and one silver coin.
  - Box C: Contains two silver coins.

A box is chosen at random, and a coin is drawn from the selected box. The question is: if the coin drawn is gold, what is the probability that the other coin in the box is also gold?

### Mathematical Framework
Using Bayes' Theorem, we calculate the conditional probability:

$$ P(G_2 | G_1) = \frac{P(G_1 | G_2) \cdot P(G_2)}{P(G_1)} $$

Where:
- $G_1$: The event that the drawn coin is gold.
- $G_2$: The event that the second coin in the same box is gold.

#### Step-by-Step Calculation:
1. **Prior Probabilities:**
   Each box is equally likely to be chosen:
   $$ P(A) = P(B) = P(C) = \frac{1}{3} $$

2. **Likelihood of Drawing a Gold Coin Given a Box:**
   - For Box A (two gold coins):
     $$ P(G_1 | A) = 1 $$
   - For Box B (one gold, one silver coin):
     $$ P(G_1 | B) = \frac{1}{2} $$
   - For Box C (two silver coins):
     $$ P(G_1 | C) = 0 $$

3. **Total Probability of Drawing a Gold Coin:**
   By the law of total probability:
   $$ P(G_1) = P(G_1 | A) \cdot P(A) + P(G_1 | B) \cdot P(B) + P(G_1 | C) \cdot P(C) $$
   Substituting the values:
   $$ P(G_1) = (1 \cdot \frac{1}{3}) + (\frac{1}{2} \cdot \frac{1}{3}) + (0 \cdot \frac{1}{3}) $$
   $$ P(G_1) = \frac{1}{3} + \frac{1}{6} + 0 = \frac{1}{2} $$

4. **Conditional Probability Calculation:**
   Using Bayes' Theorem:
   $$ P(G_2 | G_1) = \frac{P(G_1 | G_2) \cdot P(G_2)}{P(G_1)} $$
   - For Box A:
     $$ P(G_2 | G_1, A) = 1 $$
   - For Box B:
     $$ P(G_2 | G_1, B) = \frac{1}{2} $$
   - For Box C:
     $$ P(G_2 | G_1, C) = 0 $$

   Substituting values:
   $$ P(G_2 | G_1) = \frac{(1 \cdot \frac{1}{3})}{\frac{1}{2}} = \frac{2}{3}$$

#### Key Insights:
- The probability of the second coin being gold given that the first coin is gold is $$ \frac{2}{3} $$.
- This result aligns with the intuition that Box A (with two gold coins) is twice as likely to be selected when a gold coin is drawn.

### Additional Considerations:
- **Expected Values:**
  The expected value of gold coins drawn can also be calculated:
  $$ E[Gold] = P(A) \cdot 2 + P(B) \cdot 1 + P(C) \cdot 0 $$
  Substituting values:
  $$ E[Gold] = (\frac{1}{3} \cdot 2) + (\frac{1}{3} \cdot 1) + (\frac{1}{3} \cdot 0) = \frac{2}{3} + \frac{1}{3} = 1 $$

- **Variance of Gold Coins Drawn:**
  To compute the variance:
  $$ \text{Var}(Gold) = E[Gold^2] - (E[Gold])^2 $$
  Where:
  $$ E[Gold^2] = P(A) \cdot 2^2 + P(B) \cdot 1^2 + P(C) \cdot 0^2 $$
  $$ E[Gold^2] = (\frac{1}{3} \cdot 4) + (\frac{1}{3} \cdot 1) + (\frac{1}{3} \cdot 0) = \frac{4}{3} + \frac{1}{3} = \frac{5}{3} $$
  $$ \text{Var}(Gold) = \frac{5}{3} - 1^2 = \frac{5}{3} - 1 = \frac{2}{3} $$

## Folder Structure
```
project-root/
├── scripts/
│   ├── 01_generate_scenarios.py  # Generate box and coin scenarios.
│   ├── 02_run_simulations.py     # Simulate draws and record results.
│   ├── 03_analyze_results.py     # Analyze probabilities from simulations.
│   └── 04_visualize_results.py   # Create visualizations of outcomes.
├── outputs/
│   ├── simulation_results.csv    # Results from simulations.
│   ├── analysis_summary.txt      # Summary of probabilities.
│   └── visualizations/           # Folder for generated visualizations.
├── requirements.txt              # Dependencies for the project.
└── README.md                     # Project documentation.
```

## Usage
### 1. Setup the Project:
Clone the repository

Ensure you have Python installed.
Install required dependencies:
```bash
pip install -r requirements.txt
```

### 2. Run the Scripts:

#### Generate Scenarios:
Generate random box and coin scenarios:
```bash
python scripts/01_generate_scenarios.py
```

#### Run Simulations:
Simulate coin draws based on the generated scenarios:
```bash
python scripts/02_run_simulations.py
```

#### Analyze Results:
Analyze the simulation results to compute probabilities:
```bash
python scripts/03_analyze_results.py
```

#### Visualize Results:
Create visualizations for the analyzed probabilities:
```bash
python scripts/04_visualize_results.py
```

## Requirements
- Python 3.8 or later
- Required Python packages:
  - `random`
  - `csv`
  - `matplotlib`
  - `collections`

Install dependencies using the provided `requirements.txt` file.