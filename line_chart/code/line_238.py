
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
ax = plt.subplot()

ax.plot([2015, 2016, 2017, 2018, 2019], [1000, 1200, 1400, 1600, 1800], label='Solar Energy (Kwh)', color='red')
ax.plot([2015, 2016, 2017, 2018, 2019], [500, 700, 900, 1100, 1300], label='Wind Energy (Kwh)', color='green')
ax.plot([2015, 2016, 2017, 2018, 2019], [1500, 1700, 1900, 2100, 2300], label='Hydro-Energy (Kwh)', color='blue')

ax.set_xlabel('Year')
ax.set_ylabel('Energy (Kwh)')
ax.set_title('Renewable Energy Sources Usage in the United States from 2015 to 2019')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2),fancybox=True, shadow=True, ncol=3)
ax.tick_params(axis='both', which='major', labelsize=10)
ax.set_xticks([2015, 2016, 2017, 2018, 2019])
ax.tick_params(axis='both', which='minor', labelsize=8)
plt.tight_layout()
plt.savefig('line chart/png/488.png')
plt.clf()