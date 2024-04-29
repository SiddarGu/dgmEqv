
import matplotlib.pyplot as plt
plt.figure(figsize=(15, 8))
ax = plt.subplot()
ax.plot(['2020', '2021', '2022', '2023', '2024'], [2.5, 4.5, 7.5, 10.5, 12.5], label='Active Users (million)')
ax.plot(['2020', '2021', '2022', '2023', '2024'], [500, 700, 900, 1100, 1300], label='New Users (million)')
ax.plot(['2020', '2021', '2022', '2023', '2024'], [70, 75, 80, 85, 90], label='Retention Rate (%)')
plt.title('Global Social Media User Growth and Retention Rates')
plt.xlabel('Year')
plt.ylabel('Users (million), Retention Rate (%)')
plt.xticks([2020, 2021, 2022, 2023, 2024])
plt.legend(loc='upper left')
plt.grid()
for x, y1, y2, y3 in zip(['2020', '2021', '2022', '2023', '2024'], [2.5, 4.5, 7.5, 10.5, 12.5], [500, 700, 900, 1100, 1300], [70, 75, 80, 85, 90]):
    plt.annotate('(%s, %s, %s, %s)' % (x, y1, y2, y3), xy=(x, y1), xytext=(-30, 30), textcoords='offset points',
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-0.2'),
            )
plt.tight_layout()
plt.savefig('line chart/png/474.png')
plt.clf()