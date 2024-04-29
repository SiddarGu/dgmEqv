import numpy as np
import matplotlib.pyplot as plt

# Extract the data
raw_data = """Year,Coal Production (Million Tonnes),Natural Gas Production (Billion Cubic Feet),Nuclear Energy Production (Billion kWh),Hydro Energy Production (Billion kWh)
2018,5500,3500,2500,3000
2019,5600,3600,2600,3100
2020,5800,3700,2700,3300
2021,6000,3800,2800,3400
2022,6100,3900,2900,3500"""
data_lines = raw_data.split("\n")
y_values = data_lines[0].split(",")[1:]
x_values = [line.split(",")[0] for line in data_lines[1:]]
data = np.array([list(map(float, line.split(",")[1:])) for line in data_lines[1:]], dtype=np.float32)

# Create the figure and subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Create 3D bar chart
width = 0.3
colors = ['r', 'g', 'b', 'c']
for i in range(data.shape[1]):
    x = np.arange(len(x_values)) + i * width
    y = [i]*len(x_values)
    z = np.zeros(len(x_values))
    dx = width * np.ones(len(x_values))
    dy = width * np.ones(len(x_values))
    dz = data[:, i]
    color = colors[i]
    ax.bar3d(x, y, z, dx, dy, dz, color=color, alpha=0.5)

# Rotate the X-axis labels for better readability
ax.set_xticks(np.arange(len(x_values)) + width)
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values, ha='left')
    
# Adjust the viewing angles
ax.view_init(elev=20., azim=-35)

# Set the title
plt.title("Trends in Energy Production by Source - 2018 to 2022")

# Fit layout
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/200_202312302235.png")

# Clear the figure
plt.clf()
