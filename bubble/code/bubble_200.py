import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# Data in dictionary format
data_dict = [
    {"Country": "USA", "CO2 Emissions (Kilotonnes)": 5200, "Renewable Energy Use (%)": 18, "Population (Millions)": 330, "Sustainability Index": 75},
    {"Country": "China", "CO2 Emissions (Kilotonnes)": 10000, "Renewable Energy Use (%)": 23, "Population (Millions)": 1400, "Sustainability Index": 60},
    {"Country": "India", "CO2 Emissions (Kilotonnes)": 2400, "Renewable Energy Use (%)": 19, "Population (Millions)": 1380, "Sustainability Index": 62},
    {"Country": "Russia", "CO2 Emissions (Kilotonnes)": 1700, "Renewable Energy Use (%)": 16, "Population (Millions)": 120, "Sustainability Index": 65},
    {"Country": "Brazil", "CO2 Emissions (Kilotonnes)": 500, "Renewable Energy Use (%)": 45, "Population (Millions)": 213, "Sustainability Index": 90},
    {"Country": "Australia", "CO2 Emissions (Kilotonnes)": 400, "Renewable Energy Use (%)": 20, "Population (Millions)": 25, "Sustainability Index": 80},
    {"Country": "Germany", "CO2 Emissions (Kilotonnes)": 800, "Renewable Energy Use (%)": 35, "Population (Millions)": 83, "Sustainability Index": 85},
    {"Country": "Japan", "CO2 Emissions (Kilotonnes)": 1200, "Renewable Energy Use (%)": 22, "Population (Millions)": 125, "Sustainability Index": 77},
    {"Country": "Canada", "CO2 Emissions (Kilotonnes)": 600, "Renewable Energy Use (%)": 40, "Population (Millions)": 38, "Sustainability Index": 85},
    {"Country": "France", "CO2 Emissions (Kilotonnes)": 400, "Renewable Energy Use (%)": 33, "Population (Millions)": 65, "Sustainability Index": 89}
]

# Convert list of dictionaries into a DataFrame
df = pd.DataFrame(data_dict)

# Create figure and add subplot
fig, ax = plt.subplots(figsize=(12, 8))

# Normalize size of bubbles and color
size_norm = Normalize(df['Population (Millions)'].min(), df['Population (Millions)'].max())
color_norm = Normalize(df['Sustainability Index'].min(), df['Sustainability Index'].max())
cmap = get_cmap("viridis")

# Plot each data point
for i in range(df.shape[0]):
    size = size_norm(df['Population (Millions)'][i]) * 1000  # Scaling factor for bubble size
    color = cmap(color_norm(df['Sustainability Index'][i]))
    ax.scatter(df['CO2 Emissions (Kilotonnes)'][i], df['Renewable Energy Use (%)'][i], 
               s=size, color=color, alpha=0.6, edgecolors='w', linewidth=1, label=None)
    ax.scatter([], [], 
               s=20, color=color, edgecolors='w', linewidth=1, label=df['Country'][i] + f' {df["Population (Millions)"][i]}')

# Add color bar
cbar = plt.colorbar(plt.cm.ScalarMappable(norm=color_norm, cmap=cmap))
cbar.ax.get_yaxis().labelpad = 15
cbar.ax.set_ylabel('Sustainability Index', rotation=270)

# Add legend
ax.legend(title='Countries', loc='upper left')

# Set x and y labels and title
ax.set_xlabel('CO2 Emissions (Kilotonnes)')
ax.set_ylabel('Renewable Energy Use (%)')
plt.title('Sustainability Practices and CO2 Emissions by Country')

# Adding grid for better readability
ax.grid(True)

# Tight layout
plt.tight_layout()

# save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/82_202312301731.png')

# clear the current image state
plt.clf()
