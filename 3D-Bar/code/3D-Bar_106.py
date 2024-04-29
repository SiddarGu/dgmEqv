import matplotlib.pyplot as plt
import numpy as np

# Parsing raw data
raw_data = '''Year,CO2 Emission (Billion Tonnes),Forest Area (Million Hectares),Renewable Energy Consumption (Million Tonnes of oil equivalent),Solid Waste Generated (Million Tonnes)
 2015,8,10,20,24
 2016,8.5,10.5,22,24.5
 2017,9,11,23,25
 2018,9.5,11.5,24,26
 2019,10,12,25,27 '''

# Splitting raw data into lines and then to a list of lists
raw_data = list(map(lambda s: s.split(','), raw_data.split('\n')[1:-1]))

# Creating variables
x_values = [row[0].strip() for row in raw_data] # Years
y_values = list(map(str.strip, raw_data[0][1:])) # Metrics, minus 'Year'
data = np.array([list(map(float, row[1:])) for row in raw_data], dtype=np.float32) # Numeric values

# Creating 3D bar chart
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='3d')
width = 0.6 / len(y_values) # Calculating width of bars based on number of y-values (metrics)

# Plotting each column of data
for i in range(data.shape[1]):
  ax.bar3d(np.arange(len(x_values)) + i * width, [i] * len(x_values), np.zeros(len(x_values)), width, width, data[:, i], color=plt.cm.viridis(i / len(y_values)), alpha=0.8)

ax.set_title('Environment and Sustainability Metrics: 2015 to 2019')
ax.set_xticks(np.arange(len(x_values)) + width * len(y_values) / 2)
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, va='center')
ax.view_init(elev=20., azim=-35)

# Saving figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/177_202312302235.png')

# Clearing figure
plt.clf()
