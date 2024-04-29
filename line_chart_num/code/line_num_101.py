
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(15, 8))

# Data
countries = ['US', 'UK', 'France', 'Canada', 'Germany']
donors = [5000, 7000, 3000, 8000, 4000]
donation_amount = [20000, 25000, 10000, 30000, 15000]

# Create the plot
ax = fig.add_subplot(1, 1, 1)
ax.plot(countries, donors, label="Number of Donors")
ax.plot(countries, donation_amount, label="Donation Amount(dollars)")

# Label values on the plot
for i, j in enumerate(donors):
    ax.annotate(str(j), xy=(i, j + 500))

for i, j in enumerate(donation_amount):
    ax.annotate(str(j), xy=(i, j - 1000))

# Setting X and Y axis labels
ax.set_xlabel('Country')
ax.set_ylabel('Donations')

# Setting plot title
ax.set_title('Donations to International Charities from 2001 to 2005')

# Formatting the legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=5)

# Set the x ticks
plt.xticks(np.arange(len(countries)), countries, rotation=45, ha='right')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/114.png')

# Clear the current image state
plt.clf()