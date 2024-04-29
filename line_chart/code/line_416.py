
import matplotlib.pyplot as plt 

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()
ax.plot(['Red Cross', 'UNICEF', 'World Food Program', 'Global Giving', 'Operation Smile'], [4000,5000,3000,2000,1000], label="Donations", color='r', marker='o')
ax.set_title('Donations to Global Charities in 2021')
ax.set_xlabel('Organization', fontsize=10)
ax.set_xticklabels(['Red Cross', 'UNICEF', 'World\nFood Program', 'Global\nGiving', 'Operation\nSmile'], rotation=60, fontsize=10)
ax.set_ylabel('Donations', fontsize=10)
ax.grid(True, linewidth=1, linestyle='--')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('line chart/png/2.png')
plt.clf()