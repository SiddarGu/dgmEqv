
import matplotlib.pyplot as plt
import numpy as np

# Data to plot
Country = ['USA', 'UK', 'Germany', 'France']
Population = [330, 67, 83, 66]
Healthcare_Expenditure = [6000, 1500, 2000, 1400]

# Plot
fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(1, 1, 1)
ax.bar(Country, Population, label='Population(million)', bottom=0)
ax.bar(Country, Healthcare_Expenditure, label='Healthcare Expenditure(million)', bottom=Population)
ax.set_title('Healthcare Expenditure and Population in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Value')
ax.legend()

# Annotate Bar Chart
for i, v in enumerate(Population):
    ax.text(i-0.25, v+100, str(v))
for i, v in enumerate(Healthcare_Expenditure):
    ax.text(i-0.25, v+100, str(v))

# Adjust figure to avoid content from being displayed
plt.xticks(np.arange(len(Country)), Country, rotation=45)
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/487.png')

# Clear the current image state
plt.clf()