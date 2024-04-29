import matplotlib.pyplot as plt
import numpy as np


def plot_multiple_y_axes(data, data_labels, line_labels, plot_types):
    fig = plt.figure(figsize=(20, 10))
    ax1 = fig.add_subplot(111)

    columns = data.shape[1]

    for i in range(columns):
        if i == 0:
            ax = ax1
        else:
            ax = ax1.twinx()
            ax.spines["right"].set_position(("axes", 1 + 0.1 * (i - 1)))

        if plot_types[i] == "bar chart":
            ax.bar(line_labels, data[:, i], width=0.1, label=data_labels[i], color=plt.cm.Paired(i/10.), alpha=0.6)
        elif plot_types[i] == "line chart":
            ax.plot(line_labels, data[:, i], marker='o', label=data_labels[i], color=plt.cm.Paired(i/10.))
        elif plot_types[i] == "scatter chart":
            ax.scatter(line_labels, data[:, i], label=data_labels[i], color=plt.cm.Paired(i/10.))
        elif plot_types[i] == "area chart":
            ax.fill_between(line_labels, data[:, i], alpha=0.4, color=plt.cm.Paired(i/10.))
        
        ax.set_ylabel(data_labels[i])
        ax.yaxis.label.set_color(plt.cm.Paired(i/10.))
        ax.yaxis.set_major_locator(plt.MaxNLocator())
        ax.legend(loc="upper left" if i == 0 else "upper right")

    plt.title("Global Health Overview: Longevity, Accessibility, Expenditure and Physical Activity")
    plt.grid()
    plt.tight_layout()
    plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/141_202312310108.png")
    plt.clf()


line_labels = ["USA", "UK", "Germany", "Brazil", "China", "Japan", "Nigeria", "Canada", "Italy", "Australia"]
data_labels = ["Life Expectancy (Years)", "Access to Healthcare (Index Score)", 
               "Healthcare Spending (Millions of Dollars)", "Physical Activity Level (%)"]
plot_types = ["bar chart", "line chart", "scatter chart", "area chart"]

data = np.array([
    [78.86, 80, 2548, 68],
    [91.02, 85, 1406, 75],
    [90.48, 83, 3762, 82],
    [76.71, 70, 1236, 59],
    [76.91, 60, 1563, 53],
    [84.63, 88, 3374, 85],
    [53.95, 45, 976, 54],
    [92.58, 89, 2438, 82],
    [83.34, 81, 2426, 68],
    [83.94, 85, 3728, 79]
])
plot_multiple_y_axes(data, data_labels, line_labels, plot_types)
