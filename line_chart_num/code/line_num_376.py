
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 6))
ax = plt.subplot()

# Data
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Facebook Users (million)': [500, 650, 700, 850, 1000],
        'Twitter Users (million)': [500, 450, 600, 650, 750],
        'Instagram Users (million)': [400, 600, 800, 950, 1100],
        'YouTube Users (million)': [200, 300, 400, 500, 600]}

# Plot
plt.plot('Year', 'Facebook Users (million)', data=data, marker='o', markerfacecolor='blue', markersize=10, color='skyblue', linewidth=4)
plt.plot('Year', 'Twitter Users (million)', data=data, marker='o', markerfacecolor='orange', markersize=10, color='orange', linewidth=4)
plt.plot('Year', 'Instagram Users (million)', data=data, marker='o', markerfacecolor='green', markersize=10, color='green', linewidth=4)
plt.plot('Year', 'YouTube Users (million)', data=data, marker='o', markerfacecolor='red', markersize=10, color='red', linewidth=4)

# Labels
plt.title('Growth of Social Media Users from 2015 to 2019')
plt.xlabel('Year')
plt.ylabel('Users (million)')

# Legend
ax.legend()

# Data point labels
for i, txt in enumerate(data['Facebook Users (million)']):
    ax.annotate(txt, (data['Year'][i], data['Facebook Users (million)'][i]), ha='center', va='top', rotation=45)
for i, txt in enumerate(data['Twitter Users (million)']):
    ax.annotate(txt, (data['Year'][i], data['Twitter Users (million)'][i]), ha='center', va='top', rotation=45)
for i, txt in enumerate(data['Instagram Users (million)']):
    ax.annotate(txt, (data['Year'][i], data['Instagram Users (million)'][i]), ha='center', va='top', rotation=45)
for i, txt in enumerate(data['YouTube Users (million)']):
    ax.annotate(txt, (data['Year'][i], data['YouTube Users (million)'][i]), ha='center', va='top', rotation=45)

# X ticks
plt.xticks(data['Year'], data['Year'])

# Tight layout
plt.tight_layout()

# Save
plt.savefig('line chart/png/461.png', dpi=300)

# Clear
plt.clf()