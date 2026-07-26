import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set a random seed for reproducibility
np.random.seed(0)

# Generate sample data
data = np.random.normal(0, 1, 1000)

# Define 10 distinct colors
colors = plt.get_cmap('tab10').colors

# Create figure
plt.figure(figsize=(12, 7))

# Create histogram
n, bins, patches = plt.hist(
    data,
    bins=10,
    edgecolor='black',
    alpha=0.85
)

# Assign different colors to each bin
for i, patch in enumerate(patches):
    patch.set_facecolor(colors[i])

# Add frequency values above each bar
for count, left, right in zip(n, bins[:-1], bins[1:]):
    plt.text(
        (left + right) / 2,
        count + 4,
        f'{int(count)}',
        ha='center',
        fontsize=10,
        fontweight='bold'
    )

# Calculate mean and median
mean = np.mean(data)
median = np.median(data)

# Add mean line
plt.axvline(
    mean,
    linestyle='--',
    linewidth=2,
    label=f'Mean = {mean:.2f}'
)

# Add median line
plt.axvline(
    median,
    linestyle=':',
    linewidth=2,
    label=f'Median = {median:.2f}'
)

# Create smooth normal distribution curve
x = np.linspace(min(data), max(data), 500)

# Scale curve according to histogram frequency
curve = norm.pdf(x, mean, np.std(data))
curve = curve * len(data) * (bins[1] - bins[0])

plt.plot(
    x,
    curve,
    linewidth=3,
    label='Normal Distribution Curve'
)

# Add titles and labels
plt.title(
    'Histogram with 10 Bins, Different Colors and Statistics',
    fontsize=18,
    fontweight='bold'
)

plt.xlabel('Value', fontsize=13)
plt.ylabel('Frequency', fontsize=13)

# Add grid
plt.grid(axis='y', linestyle='--', alpha=0.3)

# Add legend
plt.legend()

# Improve layout
plt.tight_layout()

# Display plot
plt.show()