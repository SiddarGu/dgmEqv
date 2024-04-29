
import matplotlib.pyplot as plt
import pandas as pd

# read data
data = [['Jan',150000,200000],['Feb',200000,240000],['Mar',220000,260000],['Apr',160000,220000],['May',190000,240000],['Jun',210000,250000],['Jul',250000,300000],['Aug',210000,270000],['Sep',180000,250000],['Oct',190000,240000],['Nov',200000,250000],['Dec',240000,300000]]
df = pd.DataFrame(data, columns=['Month','Domestic Visitors','International Visitors'])

# draw figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# plot data
ax.plot(df['Month'], df['Domestic Visitors'], label='Domestic Visitors', color='#0080FF', marker='o', markersize=7)
ax.plot(df['Month'], df['International Visitors'], label='International Visitors', color='#FF8C00', marker='o', markersize=7)

# set label
ax.set_xlabel('Month', size=14)
ax.set_ylabel('Visitors', size=14)

# set title
ax.set_title('Monthly Visitors in the United States in 2021', fontsize=16, fontweight='bold')

# annotate
for i in range(len(df)):
    ax.annotate(f'D:{df["Domestic Visitors"][i]}, I:{df["International Visitors"][i]}', xy=(i-0.2, df['Domestic Visitors'][i]+20000))

# set legend & grid
ax.legend(loc='upper left', fontsize=12)
ax.grid(linestyle='--', linewidth=0.5)

# set xticks
plt.xticks(range(len(df)), df['Month'], rotation=45)

fig.tight_layout()
plt.savefig('line chart/png/73.png')
plt.clf()