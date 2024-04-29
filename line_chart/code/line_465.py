
import matplotlib.pyplot as plt

months = ['January','February','March','April','May','June','July','August']
visitors = [3000,2000,2500,2200,3000,3200,3500,3700]

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1)
ax.plot(months, visitors, color='#2F4F4F', marker='o')
ax.set_xticklabels(months, rotation=45, fontsize='large')
ax.set_title('Visitors to the Art Museum from January to August 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Visitors')
ax.grid(True, color='white')
plt.tight_layout()
plt.savefig('line chart/png/82.png')
plt.clf()