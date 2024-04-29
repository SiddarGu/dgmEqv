
import matplotlib.pyplot as plt

data = [['January', 1000], ['February', 1200], ['March', 1400], ['April', 1300], ['May', 1100], ['June', 1000], 
        ['July', 1200], ['August', 1400], ['September', 1300], ['October', 1100], ['November', 1000], ['December', 1200]]

months, emissions = zip(*data)

plt.figure(figsize=(15, 6))
ax = plt.subplot()

ax.plot(months, emissions, color='dodgerblue', linestyle='dashed', marker='o', markerfacecolor='red', markersize=8)
ax.set_title('Average CO2 Emissions in Different Months in 2021')
ax.set_xlabel('Month')
ax.set_ylabel('CO2 Emissions (tonnes)')

plt.xticks(months, rotation=45)
plt.tight_layout()

plt.savefig('line chart/png/237.png')
plt.clf()