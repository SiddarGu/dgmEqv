
plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.bar(['California','Texas','New York','Florida'], [20,22,18,21], label='Coal(million tonnes)')
ax.bar(['California','Texas','New York','Florida'], [50,48,52,49], bottom=[20,22,18,21], label='Natural Gas(million tonnes)')
ax.bar(['California','Texas','New York','Florida'], [30,32,28,31], bottom=[70,70,70,70], label='Oil(million tonnes)')
ax.set_title('Energy usage of Coal, Natural Gas, and Oil in four states in 2021')
ax.set_xticks(np.arange(4))
ax.set_xticklabels(['California','Texas','New York','Florida'])
ax.legend(loc='upper left')

# Annotate
for p in ax.patches:
    ax.annotate('{}'.format(p.get_height()), (p.get_x() + 0.225, p.get_height() + 0.5), rotation=90, fontsize=9)

plt.tight_layout()
plt.savefig('Bar Chart/png/242.png')
plt.clf()