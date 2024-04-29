
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1,1,1)

ax.set_title('Voter turnout and economic growth in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Voter Turnout and Economic Growth (%)')

Country = ['USA', 'UK', 'Germany', 'France']
Voter_Turnout = [60, 65, 70, 75]
Economic_Growth = [3.5, 2.7, 4.0, 2.4]

bar1 = ax.bar(Country, Voter_Turnout, bottom=0)
bar2 = ax.bar(Country, Economic_Growth, bottom=Voter_Turnout)

ax.legend((bar1[0], bar2[0]), ('Voter Turnout', 'Economic Growth'), bbox_to_anchor=(1.2, 0.8))


plt.xticks(Country, rotation=45, wrap=True)

plt.tight_layout()
plt.savefig('bar_65.png')
plt.clf()