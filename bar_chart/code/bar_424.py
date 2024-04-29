
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
ax = plt.subplot()
ax.set_xticks(range(4))
ax.set_xticklabels(['California', 'Texas', 'Florida', 'New York'], rotation=45, fontsize=12, wrap=True)
ax.set_title('Wind and Solar Energy Production in Four US States in 2021', fontsize=14)
ax.set_xlabel('State', fontsize=14)
ax.set_ylabel('Energy Production (kWh)', fontsize=14)
ax.bar(range(4), [3000,5000,4000,4500], color='#3266cc', width=0.4, label='Wind', bottom=0)
ax.bar(range(4), [4000,6000,3500,5500], color='#ff9933', width=0.4, label='Solar', bottom=3000)
ax.legend(loc='upper left', fontsize=14)
ax.grid(axis='y', color='#e6e6e6', linestyle='--')
plt.tight_layout()

plt.savefig('bar chart/png/381.png')
plt.clf()