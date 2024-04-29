import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker

# Parse data
data_raw = "Location,Units Sold,Units Listed,Average Selling Price (000's),Average Listing Price (000's)\nNew York City,2064,3829,1200,1500\nLos Angeles,1845,3250,1500,1900\nChicago,1400,3000,800,1250\nHouston,1300,2400,650,800\nPhoenix,1200,2250,600,850\nPhiladelphia,1100,2000,750,1100\nSan Antonio,1000,2100,500,650\nSan Diego,950,2000,1600,1700\nDallas,900,1850,750,900\nSan Jose,850,1600,2200,2350"
data_lines = data_raw.split("\n")
data_labels = data_lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in data_lines[1:]]
data = np.array([list(map(int, line.split(",")[1:])) for line in data_lines[1:]])

# Create figure and primary y-axis (ax)
fig = plt.figure(figsize=(12, 10))
ax1 = fig.add_subplot(111)
width = 0.14
ax1.bar(np.arange(len(data)) - width*2, data[:, 0], width=width, color='b', alpha=0.7)
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.set_xticks(np.arange(len(data)))
ax1.set_xticklabels(line_labels, rotation=90)
ax1.yaxis.set_major_locator(ticker.AutoLocator())

# Plot rest of the data with twinx
axes = [ax1]
for i in range(1, len(data_labels)):
    ax = axes[0].twinx()  # create a new ax using twinx
    ax.spines['right'].set_position(('outward', 60 * (i-1)))
    # plot with preferred style and set y-axis label and color accordingly
    if i == 1:
        ax.plot(np.arange(len(data)), data[:, i], color='g')
    elif i == 2:
        ax.plot(np.arange(len(data)), data[:, i], color='r')
    elif i == 3:
        ax.scatter(np.arange(len(data)), data[:, i], color='c')
    elif i == 4:
        ax.fill_between(np.arange(len(data)), 0, data[:, i], color='m', alpha=0.5)
    ax.set_ylabel(data_labels[i], color='C'+str(i))
    ax.tick_params(axis='y', labelcolor='C'+str(i))
    ax.yaxis.set_major_locator(ticker.AutoLocator())
    axes.append(ax)

plt.gca().yaxis.grid(True)
plt.title('Housing Market Data: Sales, Listings, and Pricing Trends by Location')
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/115_202312310108.png')
plt.clf()
