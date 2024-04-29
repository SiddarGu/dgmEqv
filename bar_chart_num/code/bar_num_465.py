
import matplotlib.pyplot as plt
import numpy as np

# Set data
Country = ['USA','UK', ' Germany', 'France']
Number_of_Lawyers = [55000, 40000, 30000, 35000]
Number_of_Judges = [1200, 800, 1000, 900]

# Create figure
fig, ax = plt.subplots(figsize=(10,7))

# Plot data
ax.bar(Country, Number_of_Lawyers, label='Number of Lawyers', bottom=Number_of_Judges)
ax.bar(Country, Number_of_Judges, label='Number of Judges')

# Add title and labels
ax.set_title('Number of Lawyers and Judges in Four Countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number')

# Add legend
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Labeling the value of each bar
for i, v in enumerate(Number_of_Lawyers):
    ax.text(i, v/2, str(v), ha='center', va='center', fontsize=12)
for i, v in enumerate(Number_of_Judges):
    ax.text(i, v/2, str(v), ha='center', va='center', fontsize=12)

# Set xticks
plt.xticks(np.arange(len(Country)), Country, rotation=45)

# Resize image
plt.tight_layout()

# Save as png
plt.savefig('Bar Chart/png/247.png')

# Clear the current image state
plt.clf()