
import matplotlib.pyplot as plt
import pandas as pd

data = [['Jan', 4000, 3500, 2500, 3000], ['Feb', 3000, 4000, 2800, 3200], ['Mar', 3500, 3000, 2300, 3600], ['Apr', 3800, 3200, 2500, 3500]]
df = pd.DataFrame(data, columns=['Month', 'Painting A', 'Painting B', 'Photography A', 'Photography B'])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
ax.plot(df['Month'], df['Painting A'], label='Painting A', linestyle='--', linewidth=2)
ax.plot(df['Month'], df['Painting B'], label='Painting B', linestyle='-.', linewidth=2)
ax.plot(df['Month'], df['Photography A'], label='Photography A', linestyle=':', linewidth=2)
ax.plot(df['Month'], df['Photography B'], label='Photography B', linestyle='-', linewidth=2)
ax.legend(loc='upper right', bbox_to_anchor=(1.3,1.0))
ax.grid(True)
ax.set_title('Price of Artworks and Photographs in the Year 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Price (USD)')
plt.xticks(df['Month'], rotation=45, wrap=True)
plt.tight_layout()
plt.savefig('line chart/png/254.png')
plt.clf()