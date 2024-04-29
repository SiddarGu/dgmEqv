
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# Data
country = ['USA', 'UK', 'Germany', 'France']
renewable = [150, 125, 140, 135]
coal = [200, 220, 210, 230]
oil = [120, 130, 150, 140]

# Bar Chart
ax.bar(country, renewable, label='Renewable Energy Consumption(TWh)', bottom=0)
ax.bar(country, coal, label='Coal Consumption(TWh)', bottom=renewable)
ax.bar(country, oil, label='Oil Consumption(TWh)', bottom=[sum(x) for x in zip(renewable, coal)])

# Other setting
plt.title('Energy Consumption by Renewable, Coal and Oil Sources in Four Countries in 2021')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0)
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/463.png')

# Clear current image state
plt.clf()