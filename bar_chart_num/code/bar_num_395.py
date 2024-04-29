
import matplotlib.pyplot as plt

# Create Figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Set data
Region = ["East", "West", "North", "South"]
Per_GDP = [40000, 45000, 50000, 55000]
Unemployment = [10, 12, 13, 14]

# Plotting
p1 = ax.bar(Region, Per_GDP, color='#5dade2', label='Per Capita GDP (USD)')
p2 = ax.bar(Region, Unemployment, bottom=Per_GDP, color='#f1c40f', label='Youth Unemployment Rate (%)')

# Labeling
for i, d in enumerate(Per_GDP):
    ax.annotate(str(d), xy=((i - 0.2, d / 2)), xytext=(-5, 10), textcoords='offset points')

for i, d in enumerate(Unemployment):
    ax.annotate(str(d), xy=((i - 0.2, (Per_GDP[i] + d) / 2)), xytext=(-5, 10), textcoords='offset points')

# Setting
ax.set_title('Economic performance in four regions in 2021')
ax.set_xticks(Region)
plt.legend(loc='upper center')
plt.tight_layout()

# Save
plt.savefig('Bar Chart/png/450.png')
plt.clf()