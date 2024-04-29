
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
figure(num=None, figsize=(7, 5), dpi=100, facecolor='w', edgecolor='k')
plt.bar(['USA','UK','Germany','France'], [50000,45000,40000,45500], color='#009999', label='Cases')
plt.bar(['USA','UK','Germany','France'], [8000,7500,7000,7200], bottom=[50000,45000,40000,45500], color='#0066cc', label='Lawyers')
plt.xticks(rotation=0)
plt.title('Number of legal cases and lawyers in four countries in 2021')
plt.legend()
plt.tight_layout()

for i, v in enumerate([50000,45000,40000,45500]):
    plt.text(i-.15, v/2, str(v), color='black', fontsize=10)
for i, v in enumerate([8000,7500,7000,7200]):
    plt.text(i-.15, v/2+50000, str(v), color='white', fontsize=10)

plt.savefig('Bar Chart/png/133.png')
plt.clf()