
import matplotlib.pyplot as plt
plt.figure(figsize=(12,8))
ax = plt.subplot()
x = ['USA', 'UK', 'Germany', 'France']
y_online = [50, 60, 40, 50]
y_offline = [200, 220, 180, 190]
ax.bar(x, y_online, label='Online', width=0.3, bottom=0, color='#00bfff')
ax.bar(x, y_offline, label='Offline', width=0.3, bottom=0, color='#FFA500')
ax.set_title('Number of Online and Offline Shoppers in four countries in 2021')
ax.set_ylabel('Shoppers (million)')
ax.set_xticklabels(x, rotation=45,ha='right',wrap=True)
plt.legend()
plt.tight_layout()
plt.savefig('bar chart/png/52.png')
plt.clf()