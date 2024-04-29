
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Incidence Rate (per 100k)", "Law Enforcement (Score)", "Public Opinion (Score)", "Sentencing (Score)"]
data = np.array([[300, 6, 8, 10], [240, 8, 7, 9], [570, 9, 6, 8], [140, 7, 5, 7], [100, 4, 4, 6], [80, 5, 6, 10]])
line_labels = ["Burglary", "Fraud", "Assault", "Drug Trafficking", "Money Laundering", "Tax Evasion"]

# Plot the data with the type of bubble chart
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

# Set parameters to accurately reflect the differences in data values
norm = cm.colors.Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))
s_m = cm.ScalarMappable(cmap=cm.get_cmap('RdYlBu'), norm=norm)
s_m.set_array([])
s = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (60, 500))

# Scatter each row of data
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=s[i], c=s_m.to_rgba(data[i, 3]), label=None)
    ax.scatter([], [], s=20, c=s_m.to_rgba(data[i, 3]), label=line_labels[i] + ' ' + f'{data[i, 2]}')

# Plot the legend with the title, by using ax.legend(title=data_labels[2])
ax.legend(title=data_labels[2])

# Add a color bar for the bubble colors
fig.colorbar(s_m, ax=ax, label=data_labels[3])

# Adjusting technique such as background grids and other parameter settings
ax.grid(True, linestyle='--', color='gray', alpha=0.5)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Level of Law Enforcement on Different Types of Crime in the Country')
# Resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/5_2023122261440.png')

# Set the title of the figure
plt.title("Level of Law Enforcement on Different Types of Crime in the Country")

# Clear the current image state
plt.clf()