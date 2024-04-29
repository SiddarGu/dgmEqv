

import random
import string

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def generate_random_string(length):
    """Generate a random string with the given length."""
    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(length))


# Create a dictionary with the given data
data = {"Category": ["1 Bedroom Apartments", "2 Bedroom Apartments", "3 Bedroom Apartments",
                     "1 Bedroom Houses", "2 Bedroom Houses", "3 Bedroom Houses",
                     "4 Bedroom Houses", "5+ Bedroom Houses"],
        "Median House Price ($)": [200000, 250000, 300000,
                                   350000, 400000, 450000,
                                   500000, 550000],
        "Median Household Income ($)": [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000]}

# Convert the first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size and background grid lines
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.grid(linestyle='--', linewidth=0.5, color='#d3d3d3')

# Set the x and y axis ticks and ticklabels
if random.random() < 0.7:
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0], wrap=True, rotation=45, ha='right', rotation_mode='anchor')
    ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
else:
    ax.set_xticks([])
    ax.set_yticks([])

# Set the labels and plot the data
ax.set_xlabel("Category")
ax.set_ylabel("Median House Price ($)")
ax.set_title("Real Estate Trends and Housing Market Analysis")
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2],
             colors=['#ff8c00', '#ffa500', '#ffd700', '#ffebcd'],
             labels=['Median House Price ($)', 'Number of Houses Sold', 'Median Household Income ($)', 'Average Mortgage Rate (%)'],
             alpha=0.7)

# Set the legend's position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Automatically resize the image and save it
fig.tight_layout()
fig.savefig('output/final/area_chart/png/20231228-145339_85.png', bbox_inches='tight')

# Clear the current image state
plt.clf()