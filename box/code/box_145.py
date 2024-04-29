
import matplotlib.pyplot as plt
import numpy as np

data = {"Voter Turnout Rate" : ["State A", "State B", "State C", "State D", "State E"],
        "Min Rate (Percent)": [30, 40, 45, 25, 35],
        "Q1 Rate (Percent)": [50, 55, 60, 45, 50],
        "Median Rate (Percent)": [60, 65, 70, 60, 65],
        "Q3 Rate (Percent)": [75, 80, 80, 75, 80],
        "Max Rate (Percent)": [85, 90, 95, 85, 90],
        "Outlier Rate (Percent)": [[], [95], [10,25], [95], [100]]}

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

statenames = np.array(data["Voter Turnout Rate"])

quartiles = np.array([data["Min Rate (Percent)"], data["Q1 Rate (Percent)"], 
             data["Median Rate (Percent)"], data["Q3 Rate (Percent)"],
             data["Max Rate (Percent)"]])

bp = ax.boxplot(quartiles, labels=statenames)

for i, outlier in enumerate(data["Outlier Rate (Percent)"]):
    for j in outlier:
        ax.plot(i+1, j, 'ro')

ax.set_title("Voter Turnout Rate Distribution Among States in 2020", fontsize=16)
ax.set_xticklabels(statenames, rotation=45, ha="right", fontsize=14)
ax.set_ylabel("Rate (Percent)", fontsize=14)

fig.tight_layout()
fig.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/1_202312251044.png")
plt.clf()