import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_values = [
    [2400],
    [1800],
    [800],
    [600],
    [500],
    [700],
    [400],
    [300]
]
data_labels = ["Electricity Production (TWh)"]
line_labels = [
    "Coal",
    "Natural Gas",
    "Nuclear",
    "Hydro",
    "Solar",
    "Wind",
    "Biomass",
    "Geothermal"
]

# Transforming data into DataFrame
data_dict = {data_labels[0]: [row[0] for row in data_values]}
df = pd.DataFrame(data_dict, index=line_labels)

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

df.plot(kind='bar', ax=ax, color='skyblue', grid=True)

# Setting title, labels, and rotating x-tick labels
ax.set_title('Annual Electricity Production by Energy Source')
ax.set_xlabel('Energy Source')
ax.set_ylabel('Electricity Production (TWh)')
plt.xticks(rotation=45, ha='right', wrap=True)

# Adjusting layout
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/60.png')

# Clear the current figure's state
plt.clf()
