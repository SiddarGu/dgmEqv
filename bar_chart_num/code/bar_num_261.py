
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Hotel_Rooms = [20000, 30000, 18000, 23000]
Tourist_Visits = [40000, 50000, 40000, 47000]

x = np.arange(len(Country))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x - width/2, Hotel_Rooms, width, label='Hotel Rooms')
ax.bar(x + width/2, Tourist_Visits, width, label='Tourist Visits')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.set_title('Number of hotel rooms and tourist visits in four countries in 2021')
ax.legend()

for i, v in enumerate(Hotel_Rooms):
    ax.text(x[i] - width/2, v+1000, str(v), color='blue', fontweight='bold')
for i, v in enumerate(Tourist_Visits):
    ax.text(x[i] + width/2, v+1000, str(v), color='red', fontweight='bold')

plt.tight_layout()
plt.savefig('Bar Chart/png/361.png')
plt.clf()