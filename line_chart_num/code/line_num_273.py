
import matplotlib.pyplot as plt
import numpy as np

# create figure
fig = plt.figure(figsize=(15,6))
ax = fig.add_subplot(111)

# data
x_data = np.array([2018, 2019, 2020, 2021, 2022, 2023])
y1_data = np.array([400, 450, 500, 525, 550, 575])
y2_data = np.array([500, 550, 600, 625, 650, 675])

# plot
ax.plot(x_data, y1_data, label='Average Price', color='#008080')
ax.plot(x_data, y2_data, label='Number of Homes Sold', color='#FFA500')

# legend
plt.legend(loc='best', frameon=True)

# annotate
for x, y1, y2 in zip(x_data, y1_data, y2_data):
    plt.annotate(y1, xy=(x, y1), ha='center', va='bottom', fontsize=12, color='#008080')
    plt.annotate(y2, xy=(x, y2), ha='center', va='bottom', fontsize=12, color='#FFA500')

# title
plt.title('Average Home Prices and Number of Homes Sold in the US from 2018 to 2023', fontsize=14, fontweight='bold')

# xticks
plt.xticks(x_data, rotation=45, fontsize=12)

# tight_layout
plt.tight_layout()

# save
plt.savefig('line chart/png/197.png')

# clear
plt.clf()