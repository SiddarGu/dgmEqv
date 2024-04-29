
import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(6, 4))

# Set bar chart
Country = ['USA', 'UK', 'Germany', 'France']
GDP_investment = [400, 350, 320, 340]
Research_grants = [50, 40, 45, 60]
Scientists = [10000, 8000, 7000, 9000]

x = np.arange(len(Country))
width = 0.2

ax = plt.subplot()
ax.bar(x - width, GDP_investment, width=width, label='GDP Investments(billion)', color='orange')
ax.bar(x, Research_grants, width=width, label='Research Grants(million)', color='lightblue')
ax.bar(x + width, Scientists, width=width, label='Scientists', color='lightgreen')

# Set x-axis, y-axis, and legend
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.set_ylabel('Amount')
ax.set_title('Science and Engineering investments and resources in four countries in 2021')
ax.legend()

# Adjust the display of the chart
plt.tight_layout()

# Save the chart
plt.savefig('bar chart/png/559.png')

# Clear the current image state
plt.clf()