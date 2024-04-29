
import matplotlib.pyplot as plt
import numpy as np

# Get data
age = ['18-24', '25-34', '35-44', '45-54', '55-64']
percentage = [25, 20, 25, 20, 10]

# Create figure
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111)

# Plot data
ax.pie(percentage, labels=age, autopct='%1.1f%%', textprops={'fontsize': 12}, shadow=True, startangle=90, pctdistance=0.8)

# Set title
ax.set_title("Technology Usage Among Different Age Groups in the USA, 2023", fontsize=16, fontweight='bold')

# Adjust plot
plt.tight_layout()
plt.xticks(rotation=90)

# Save figure
fig.savefig('pie chart/png/239.png')

# Clear current image state
plt.clf()