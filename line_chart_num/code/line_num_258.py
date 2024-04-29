
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,13)
y1 = [50, 55, 60, 65, 70, 72, 75, 80, 85, 90, 95, 100]
y2 = [20, 22, 25, 30, 32, 35, 37, 40, 45, 48, 50, 55]
y3 = [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520]

fig, ax = plt.subplots(figsize=(11,7))
ax.plot(x, y1, label='Number of Art Galleries', linewidth=3)
ax.plot(x, y2, label='Number of Art Exhibitions', linewidth=3)
ax.plot(x, y3, label='Number of Artworks', linewidth=3)

plt.xticks(x)
ax.set_title('Increase in Art-related activities in the United States from 2021 to 2022', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=14, fontweight='bold')
ax.set_ylabel('Number', fontsize=14, fontweight='bold')

for a,b,c,d in zip(x, y1, y2, y3):
    ax.annotate(f'{d}', xy=(a,d), xytext=(a,d+10), fontsize=12, fontweight='bold')
    ax.annotate(f'{b}', xy=(a,b), xytext=(a,b+10), fontsize=12, fontweight='bold')
    ax.annotate(f'{c}', xy=(a,c), xytext=(a,c+10), fontsize=12, fontweight='bold')

ax.legend(loc='upper left', fontsize=13)
ax.grid(True, linestyle='-.', color='#f2f2f2')
plt.tight_layout()
plt.savefig('line chart/png/367.png')
plt.clf()