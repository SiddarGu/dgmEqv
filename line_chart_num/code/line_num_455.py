
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
ax = plt.subplot()

x_axis = ['0-5','6-10','11-15','16-20','21-25']
vaccination_rate = [90,92,94,96,98]
mortality_rate = [0.03,0.02,0.01,0.01,0.005]

ax.plot(x_axis, vaccination_rate, label = 'Vaccination Rate(%)', color = 'green')
ax.plot(x_axis, mortality_rate, label = 'Mortality Rate', color = 'red')

ax.legend(loc = 'upper right')
plt.title('Vaccination and mortality rate of different age groups in the United States')

plt.xlabel('Age')
plt.ylabel('Rate(%)')

for i in range(len(x_axis)):
    ax.annotate(vaccination_rate[i], (x_axis[i], vaccination_rate[i]))
    ax.annotate(mortality_rate[i], (x_axis[i], mortality_rate[i]))

plt.xticks(x_axis, rotation=45)
plt.tight_layout()
plt.savefig('line chart/png/527.png')
plt.clf()