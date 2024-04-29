import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.dates import AutoDateLocator

# Parse the raw string data
raw_data = "Year,Number of cases,Amount involved (Millions),Bail posted (Thousands)/n 2015,950,5000,2980/n 2016,1020,5200,3040/n 2017,1200,5340,3200/n 2018,1370,5560,3290/n 2019,1500,5800,3500/n 2020,1450,6100,3400/n 2021,1300,4990,2700"
raw_data = raw_data.split("/n ")

# Data prep
data = []
for row in raw_data:
    data.append(row.split(","))
    
df = pd.DataFrame(data[1:], columns=data[0])
df = df.apply(pd.to_numeric)

# Data variables
line_labels = df['Year'].values
data_labels = df.columns[1:].tolist()
data = df[data_labels].values.T
colors = ['r', 'g', 'b']

# Plot
fig = plt.figure(figsize=[25, 10])
ax = fig.add_subplot(111)

for idx, (row_data, row_label, color_val) in enumerate(zip(data, data_labels, colors)):
    if idx == 0:
        ax.plot(line_labels, row_data, label=row_label, color=color_val)
        ax.set_ylabel(row_label, color=color_val)
    else:
        ax_new = ax.twinx()
        if idx == 1:
            ax_new.fill_between(line_labels, row_data, color=color_val, alpha=0.4, label=row_label)
        else:
            ax_new.bar(line_labels, row_data, color=color_val, alpha=0.7, label=row_label)
        ax_new.set_ylabel(row_label, color=color_val)
        ax_new.yaxis.label.set_color(color_val)
        ax_new.spines['right'].set_position(('outward', (idx-1)*60))

# Title
plt.title("Analysis of Legal Cases, Financial Involvement and Bail Posted Over the Years")

# Legends
fig.legend(loc="upper right", bbox_to_anchor=(1,1))

# Grid
ax.grid()

# Autoscale all y-axes
for axes in fig.get_axes():
    axes.autoscale_view()

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/175_202312310108.png', orientation='landscape')

# Clear current figure
plt.clf()
