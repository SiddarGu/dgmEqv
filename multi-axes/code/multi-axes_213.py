import matplotlib.pyplot as plt
import numpy as np

# Prepare data
data_str = """Dairy Products,4200,2200,5
Processed Meats,6100,2100,11
Alcoholic Beverages,3750,1700,10
Non-Alcoholic Drinks,8000,3500,4
Fruits & Vegetables,4900,3330,3
Coffee,2968,1640,10
Tea,2128,1480,12
Bakeries & Tortillas,7850,4365,6
Seafood,5830,3100,18
Chocolate & Confectionery,5200,1850,15"""

data_lines = data_str.split("\n")
line_labels = [line.split(",")[0] for line in data_lines]
data = np.array([list(map(float, line.split(",")[1:])) for line in data_lines])
data_labels = ["Annual Sales (Millions)", "Exports (Millions)", "Average Price (Dollars per Kilo)"]

# set plot type
plot_types = ["bar", "line", "scatter"]

# Create figure
fig = plt.figure(figsize=(25,10))
ax1 = fig.add_subplot(111)

# Plot first column
ax1.bar(line_labels, data[:,0], color="blue", alpha = 0.6, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color="blue")
ax1.set_title("Food and Beverage Industry: Sales, Exports, and Price Overview")
ax1.legend(loc="upper left")

# Plot rest columns
axes = [ax1]
colors = ['red', 'green', 'purple']
for i in range(1, data.shape[1]):
    ax = axes[0].twinx()
    if plot_types[i] == "line":
        ax.plot(line_labels, data[:,i], color=colors[i], label=data_labels[i])
    elif plot_types[i] == 'bar':
        ax.bar(line_labels, data[:,i], color=colors[i], alpha = 0.6, label=data_labels[i])
    else:
        ax.scatter(line_labels, data[:,i],color=colors[i], label=data_labels[i])
        
    ax.set_ylabel(data_labels[i], color=colors[i])
    ax.spines['right'].set_position(("axes", i*0.15))
    ax.legend(loc="upper right")
    axes.append(ax)

plt.tight_layout()
plt.grid()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/241_202312311051.png")
plt.show()
plt.clf()
