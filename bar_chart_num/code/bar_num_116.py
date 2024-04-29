
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 5)) 
ax = fig.add_subplot(111)

Country = ['USA', 'UK', 'Germany', 'France']
Education = [90, 87, 80, 85]
Healthcare = [85, 83, 82, 85]
Public_Safety = [95, 93, 92, 90]

width = 0.2
ind = np.arange(len(Country)) 

p1 = ax.bar(ind, Education, width, color='#539caf', label='Education')
p2 = ax.bar(ind + width, Healthcare, width, color='#7663b0', label='Healthcare')
p3 = ax.bar(ind + (2 * width), Public_Safety, width, color='#ff8a5c', label='Public Safety')

ax.set_title('Indicators of social services in four countries in 2021', fontsize=14)
ax.set_xticks(ind + width)
ax.set_xticklabels(Country)
ax.legend(loc='upper center')

for rect in p1 + p2 + p3:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height / 2),
                xytext=(0, 3), 
                textcoords="offset points",
                ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.savefig('Bar Chart/png/109.png', dpi=100)
plt.clf()