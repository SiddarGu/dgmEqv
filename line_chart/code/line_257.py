
import matplotlib.pyplot as plt

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
online_shopping = [60, 65, 70, 72, 75, 80, 82, 85]
offline_shopping = [40, 35, 30, 28, 25, 20, 18, 15]

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot()
ax.plot(month, online_shopping, label='Online Shopping')
ax.plot(month, offline_shopping, label='Offline Shopping')
ax.set_title('Percentage of Online and Offline Shopping in 2020')
ax.set_xlabel('Month')
ax.set_ylabel('Percentage(%)')
ax.legend(loc='best', ncol=2, framealpha=0.5, fontsize=10, labelspacing=1.2, columnspacing=1.2)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('line chart/png/361.png')
plt.clf()