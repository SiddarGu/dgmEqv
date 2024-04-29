
import matplotlib.pyplot as plt
import numpy as np

# Data
age = np.array([18, 19, 20, 21, 22, 23, 24])
weight = np.array([75, 72, 80, 78, 77, 76, 74])
height = np.array([180, 175, 182, 179, 178, 177, 176])

# Create figure
plt.figure(figsize=(8, 6))

# Plot
plt.plot(age, weight, label="Weight (kg)")
plt.plot(age, height, label="Height (cm)")

# Annotate
for i, j in zip(age, weight):
    plt.annotate(str(j), xy=(i, j))
for i, j in zip(age, height):
    plt.annotate(str(j), xy=(i, j))

# Label
plt.title("Weight and Height changes of people aged 18-24")
plt.xlabel("Age")
plt.ylabel("Weight/Height (kg/cm)")

# xticks
plt.xticks(age)

# Legend
plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1.0))

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/555.png')

# Clear figure
plt.clf()