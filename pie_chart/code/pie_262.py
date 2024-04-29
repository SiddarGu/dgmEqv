
import matplotlib.pyplot as plt
import numpy as np

# Create figure and add subplot
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)

# Data
labels = ['Civil Cases', 'Criminal Cases', 'Regulatory Cases', 'International Cases', 'Other Cases']
data = [30, 30, 15, 20, 5]

# Plot
ax.pie(data, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 10, 'wrap': True, 'rotation': 20}, startangle=90, colors=['#566f9f', '#ed553b', '#e4a14b', '#c6d2d5', '#c5e3bf'])

# Title
ax.set_title("Types of Cases Handled by the Legal System in the USA, 2023", fontsize=14, pad=20)

# Save and display 
plt.tight_layout()
plt.savefig('pie chart/png/518.png')
plt.clf()