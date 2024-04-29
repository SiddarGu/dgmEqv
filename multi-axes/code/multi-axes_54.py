import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Data preparation
raw_data = """Organization,Total Donors,Total Funds Raised (Thousands),Number of Events
United Way Worldwide,140,10300,25
Task Force for Global Health,75,7050,7
Feeding America,200,12000,70
Salvation Army,300,8000,95
St. Jude Children's Research Hospital,400,10700,50
American Cancer Society,275,5500,30
Direct Relief,100,4000,18
Make-A-Wish Foundation,350,7500,62
Doctors Without Borders,130,6000,20
YMCA,290,8500,45"""
data = np.genfromtxt(raw_data.split("\n")[1:], delimiter=",", names=True, dtype=None)
line_labels = [row[0] for row in data]
data = np.array([list(row)[1:] for row in data])
data_labels = raw_data.split("\n")[0].split(",")[1:]

# Figure preparation
fig = plt.figure(figsize=(20, 10))

colors = ['r', 'g', 'b', 'y']
axes = []
for i in range(data.shape[1]):
    if i == 0:
        axes.append(fig.add_subplot(111))
    else:
        axes.append(axes[0].twinx())

# Each column of data is plotted with a different type and y-axis.
for i, ax in enumerate(axes):
    if i == 0:
        ax.bar(line_labels, data[:,i], color=colors[i], alpha=0.6, align="center")
    elif i == 1:
        ax.plot(line_labels, data[:,i], color=colors[i])
    elif i == 2:
        ax.scatter(line_labels, data[:,i], color=colors[i])
    elif i == 3:
        ax.fill_between(line_labels, 0, data[:,i], color=colors[i], alpha=0.5)

    ax.yaxis.label.set_color(colors[i])
    ax.spines['right'].set_position(('outward', (i-1)*60))
    if i > 1:
        ax.spines['right'].set_color(colors[i])
    ax.set_xlabel("Organization")
    ax.set_ylabel(data_labels[i])
    ax.yaxis.set_major_locator(ticker.AutoLocator())
    ax.legend([data_labels[i]], loc=i+1)

plt.title("Donor Engagement and Fundraising across Multiple Charities")
fig.autofmt_xdate()
fig.tight_layout()
plt.grid(True)
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/102_2023122292141.png")
plt.clf()
