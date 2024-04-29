
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

regions = ['North America', 'South America', 'Europe', 'Asia']
renewable_energy = [20, 35, 40, 30]
non_renewable_energy = [80, 65, 60, 70]

x_pos = range(len(regions))

ax.bar(x_pos, renewable_energy, width=0.5, color='green', label='Renewable energy sources')
ax.bar([p + 0.5 for p in x_pos], non_renewable_energy, width=0.5, color='red', label='Non-renewable energy sources')

# Set labels and ticks
ax.set_xticks([p + 0.5 for p in x_pos])
ax.set_xticklabels(regions)
ax.set_ylabel('Percentage (%)')
ax.set_title('Percentage of Renewable and Non-Renewable Energy Sources in Different Regions in 2021')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)

# Label each bar
for i in range(len(regions)):
    ax.annotate(str(renewable_energy[i]) + '%', xy=(x_pos[i] - 0.25, renewable_energy[i] + 1), rotation=90, size=12)
    ax.annotate(str(non_renewable_energy[i]) + '%', xy=(x_pos[i] + 0.25, non_renewable_energy[i] + 1), rotation=90, size=12)

# Adjust the image size
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/414.png')

# Clear the current state of the figure
plt.clf()