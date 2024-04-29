
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot()

Country =['USA', 'UK', 'Germany', 'France']
Donations = [500, 300, 400, 250]
Volunteers = [10000, 9000, 8000, 7000]

ax.bar(Country, Donations, bottom = 0, label='Donations', width = 0.3, color='#F78F1E')
ax.bar(Country, Volunteers, bottom = 0, label='Volunteers', width = 0.3, color='#581845')

ax.set_xticks(Country)
ax.set_title('Donations and Volunteers for Nonprofit Organizations in Four Countries in 2021')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.savefig('bar chart/png/70.png')
plt.clf()