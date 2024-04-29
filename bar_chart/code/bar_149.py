
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111)

# Draw the bar chart
country = ['USA', 'UK', 'Germany', 'France']
data = [3.6, 1.2, 1.9, 1.5]
ax.bar(country, data, width=0.4, color='b', align='center')

# Set the parameters of the chart
plt.title('Population and Public Expenditure on Education in four countries in 2021', fontsize=10)
plt.xlabel('Country', fontsize=10)
plt.ylabel('Public Expenditure on Education(billion)', fontsize=10)
ax.set_xticks(country)
plt.tight_layout()

# Save the figure
plt.savefig('bar chart/png/152.png')

# Clear the current image state
plt.clf()