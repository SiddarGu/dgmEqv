
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {"Category": ["Primary Care", "Surgery", "Emergency Care", "Rehabilitation", "Mental Health", "Maternity Care", "Cancer Care", "Wellness", "Dental Care", "Elderly Care"],
        "Preventive Care (%)": [50, 30, 20, 10, 20, 40, 20, 50, 40, 30],
        "Treatment (%)": [30, 40, 20, 20, 30, 40, 30, 20, 20, 10],
        "Medication (%)": [10, 10, 40, 40, 30, 10, 30, 20, 30, 40],
        "Diagnostic Tests (%)": [10, 20, 20, 30, 20, 10, 20, 10, 10, 20]}

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Set axis labels and title
ax.set_xlabel("Category")
ax.set_ylabel("Percentage")
ax.set_title("Healthcare Services Breakdown by Category")

# Set x and y axis ticks and ticklabels with 70% probability
if np.random.choice([0, 1]) == 1:
    ax.set_xticks(np.arange(len(df)))
    ax.set_xticklabels(df["Category"])

if np.random.choice([0, 1]) == 1:
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    # Round up max total value to nearest multiple of 10, 100, or 1000
    if max_total_value < 100:
        max_total_value = np.ceil(max_total_value / 10) * 10
    elif max_total_value < 1000:
        max_total_value = np.ceil(max_total_value / 100) * 100
    else:
        max_total_value = np.ceil(max_total_value / 1000) * 1000
    # Set y limits and ticks with length in list of [3, 5, 7, 9, 11]
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

plt.xticks(rotation=90, ha='right', rotation_mode='anchor')
# Set background grid lines
ax.grid(color="lightgrey", linestyle="--", linewidth=0.5, alpha=0.5)

# Plot data with area chart
ax.stackplot(df["Category"], df["Preventive Care (%)"], df["Treatment (%)"], df["Medication (%)"], df["Diagnostic Tests (%)"],
             labels=["Preventive Care", "Treatment", "Medication", "Diagnostic Tests"],
             colors=["#8dd3c7", "#ffffb3", "#bebada", "#fb8072"],
             alpha=0.8)

# Set legend and position
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

# Resize image by tight_layout()
plt.tight_layout()

# Save figure
plt.savefig("output/final/area_chart/png/20231228-145339_16.png", bbox_inches="tight")

# Clear current image state
plt.clf()