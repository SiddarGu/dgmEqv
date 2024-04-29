
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import colorConverter
import numpy as np

data_labels = ['Median Home Prices', 'Average Rental Rates', 'Homeownership Rate', 'Vacancy Rate', 'Foreclosures']
line_labels = ['Category', 'ratio']
data = [30, 10, 25, 15, 20]

fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(111)

# Set the data labels and line labels
ax.set_xlabel('Category', fontsize=12)
ax.set_ylabel('Ratio (%)', fontsize=12)

# Set the data
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=[colorConverter.to_rgba(c) for c in ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']])

# Create the inner circle
inner_circle = plt.Circle((0,0), 0.65, color='white')
ax.add_artist(inner_circle)

# Set the legend
ax.legend(data_labels, bbox_to_anchor=(1.25, 1))

# Title and save
plt.title('Real Estate and Housing Market Overview - 2023', fontsize=14)
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_94.png")
plt.clf()