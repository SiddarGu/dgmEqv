# Re-importing necessary libraries after the reset
import matplotlib.pyplot as plt
import numpy as np

# Data and labels
data_labels = ["Category", "Cases Filed (Thousands)", 
               "Court Cases Settled (Thousands)",
               "Lawyers Per Capita", "Average Length of Suit (Months)"]
line_labels = ["Civil Cases", "Criminal Cases", "Family Law Cases", 
               "Immigration Law Cases", "Bankruptcy Cases", 
               "Tax Law Cases", "Contract Law Cases", 
               "Employment Law Cases", "Patent Law Cases",
               "Intellectual Property Cases"]
data = np.array([[645, 379, 3.2, 12],
                 [724, 541, 1.6, 15],
                 [321, 258, 2.4, 24],
                 [567, 267, 1.4, 18],
                 [367, 198, 2.8, 6],
                 [156, 138, 1.9, 16],
                 [189, 145, 2.1, 14],
                 [285, 162, 2.3, 7],
                 [124, 109, 1.2, 20],
                 [122, 98, 1.5, 10]])

# Setting up the figure
fig, ax = plt.subplots(figsize=(14, 8))

# Initial bar plot and axis
bar_width = 0.15
bar_pos = np.arange(len(line_labels))
ax.bar(bar_pos - 1.5*bar_width, data[:, 0], width=bar_width, label=data_labels[1], color='C0')

# Additional axes for other data series
for i in range(2, data.shape[1] + 1):
    ax_new = ax.twinx()  # Create a new axis
    offset = (i - 2) * 60  # Offset for each new axis
    ax_new.spines['right'].set_position(('outward', offset))
    ax_new.bar(bar_pos - 1.5*bar_width + (i - 1)*bar_width, data[:, i - 1], width=bar_width, label=data_labels[i], color='C' + str(i))

    ax_new.set_ylabel(data_labels[i])
    ax_new.yaxis.label.set_color('C' + str(i))

# Setting the x-axis labels
ax.set_xticks(bar_pos)
ax.set_xticklabels(line_labels, rotation=45)
ax.set_ylabel(data_labels[1])

# Add the title of the figure
plt.title("Analysis of Legal Cases Filed and Settled in the Courts: Volume and Duration")

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/7.png")

# Clear the current image state
plt.clf()