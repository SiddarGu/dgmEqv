
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

#Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Output Capacity (Megawatts)", "Efficiency (%)", "Environmental Impact (Score)", "Cost (Billion $)"]
line_labels = ["Coal", "Wind", "Solar", "Nuclear", "Hydro"]
data = np.array([[4500, 40, 200, 2.4],
                 [3000, 60, 500, 1.8],
                 [1200, 80, 1000, 1.2],
                 [2500, 95, 100, 3.5],
                 [1500, 85, 300, 2.0]])

#Plot the data with the type of bubble chart
fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot()

#Normalize the color and size
norm = mpl.colors.Normalize(vmin = data[:,-1].min(), 
                            vmax = data[:,-1].max())
s_m = mpl.cm.ScalarMappable(cmap="RdYlGn", norm=norm)
s_m.set_array([])

sizes = np.linspace(600, 5000, data.shape[0])

#Plotting using plt.scatter
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], 
               s=sizes[i], 
               c=s_m.to_rgba(data[i, -1]), 
               label=None)
    ax.scatter([], [], c=s_m.to_rgba(data[i, -1]), label=line_label + " " + str(data[i, 2]), s=20)

#Plot the legend with the title
ax.legend(title=data_labels[2])

#Add a color bar for the bubble colors
cbar = fig.colorbar(s_m, ax=ax)
cbar.ax.set_ylabel(data_labels[3], rotation=-90, va="bottom")

#Adjust the figure view
ax.set_title("Efficiency and Cost of Various Power Plants - Energy and Utilities 2023")
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(True)

#Automatically resize the image
plt.tight_layout()

#Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/2_2023122261326.png")

#Clear the current image state
plt.clf()