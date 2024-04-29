
import matplotlib.pyplot as plt

# Create figure
plt.figure(figsize=(10, 6))

# Create data
Region = ["North America", "Europe", "Asia", "South America"]
Solar_Energy = [150, 180, 200, 120]
Wind_Energy = [200, 220, 240, 180]
Hydropower_Energy = [100, 110, 120, 90]

# Create bars
x_pos = list(range(len(Region)))
width = 0.2

# Plotting bars
plt.bar(x_pos, Solar_Energy, width, label='Solar Energy(Million kWh)', color='orange')
plt.bar([p + width for p in x_pos], Wind_Energy, width, label='Wind Energy(Million kWh)', color='green')
plt.bar([p + width*2 for p in x_pos], Hydropower_Energy, width, label='Hydropower Energy(Million kWh)', color='blue')

# Setting axis labels and ticks
plt.xticks([p + width for p in x_pos], Region, fontsize=10)
plt.yticks(fontsize=10)

# Adding legend and title
plt.title("Energy production from solar, wind and hydropower in different regions in 2021", fontsize=15)
plt.legend(bbox_to_anchor=(1, 1), fontsize=10)

# Labeling value of each data point in the bar
for i, v in enumerate(Solar_Energy):
    plt.text(x_pos[i]-0.05, v+3, str(v), fontsize=10)
for i, v in enumerate(Wind_Energy):
    plt.text(x_pos[i]+0.15, v+3, str(v), fontsize=10)
for i, v in enumerate(Hydropower_Energy):
    plt.text(x_pos[i]+0.33, v+3, str(v), fontsize=10)

# Adjusting layout
plt.tight_layout()   

# Saving figure
plt.savefig('Bar Chart/png/496.png')

# Clear current image state
plt.clf()