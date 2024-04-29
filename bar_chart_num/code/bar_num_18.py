
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1, 1, 1)

# Set the bar chart parameters
Country = ['USA','UK','Germany','France']
CO2_Emissions = [20000,18000,22000,21000]
Renewable_Energy_Usage = [10,20,15,25]
Air_Quality_Index = [30,40,50,60]

bar_width = 0.2
index = np.arange(len(Country))

# Plot bars
ax.bar(index, CO2_Emissions, bar_width, label='CO2 Emissions (tonnes)', color='r')
ax.bar(index+bar_width, Renewable_Energy_Usage, bar_width, label='Renewable Energy Usage (%)', color='b')
ax.bar(index+2*bar_width, Air_Quality_Index, bar_width, label='Air Quality Index', color='g')

# Set the x-axis
plt.xticks(index + bar_width, Country)
plt.xlabel("Country")

# Set the y-axis
ax.set_ylabel("Value")

# Set the legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=4)

# Add the title
plt.title('Environmental indicators of four countries in 2021')

# Add the value of each data point to the plot
for x, y in zip(index + bar_width, CO2_Emissions):
    plt.annotate(str(y), xy=(x, y), xytext=(0, 0), textcoords="offset points", ha='center', va='bottom')
for x, y in zip(index + bar_width, Renewable_Energy_Usage):
    plt.annotate(str(y), xy=(x, y), xytext=(0, 0), textcoords="offset points", ha='center', va='bottom')
for x, y in zip(index + bar_width, Air_Quality_Index):
    plt.annotate(str(y), xy=(x, y), xytext=(0, 0), textcoords="offset points", ha='center', va='bottom')

# Adjust the padding and save the image
plt.tight_layout()
plt.savefig('Bar Chart/png/548.png')

# Clear the current image state
plt.clf()