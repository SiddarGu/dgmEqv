
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 8))
ax = plt.subplot()
plt.title('Energy consumption of electricity and gas from January to April 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Consumption (MWh)')
x = ["January", "February", "March", "April"]
y1 = [1800, 1700, 1900, 2000]
y2 = [1200, 1400, 1300, 1500]

plt.xticks(range(len(x)), x)
ax.bar(x, y1, label='Electricity', bottom=y2, color='darkred')
ax.bar(x, y2, label='Gas', color='darkblue')

for i in range(len(x)):
    plt.text(x=i-0.2, y=y1[i]+y2[i]+20, s="{}".format(y1[i]+y2[i]), color='black', fontsize=10, fontweight='bold')

plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('Bar Chart/png/549.png')
plt.clf()