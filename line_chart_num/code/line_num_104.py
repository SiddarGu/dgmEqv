
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Arial'
plt.figure(figsize=(10,6))
ax = plt.subplot(111)
x = [2020, 2021, 2022, 2023]
Youtube = [3, 3.5, 4, 4.5]
Facebook = [2, 2.5, 3, 3.5]
Twitter = [1, 1.2, 1.5, 2]
ax.plot(x, Youtube, label='Youtube Views')
ax.plot(x, Facebook, label='Facebook Visits')
ax.plot(x, Twitter, label='Twitter Visits')
ax.annotate('Youtube Views(billion)', xy=(2023, 4.5), xytext=(2020, 4.8),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Facebook Visits(billion)', xy=(2023, 3.5), xytext=(2020, 3.8),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Twitter Visits(billion)', xy=(2023, 2), xytext=(2020, 2.3),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.title('Social Media Platforms Visits from 2020 to 2023', fontsize=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Views(billion)', fontsize=12)
plt.xticks(x)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()
plt.savefig('line chart/png/177.png')
plt.clf()