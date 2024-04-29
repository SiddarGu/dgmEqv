
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.set_title("Average BMI of Different Age Groups in the United States")

plt.plot(['18-24', '25-34', '35-44', '45-54', '55-64', '65-74'], 
         [21.5, 23.7, 26.2, 27.3, 27.8, 27.9], marker='o', 
         color='b', label='Average BMI')
ax.set_xticklabels(['18-24', '25-34', '35-44', '45-54', '55-64', '65-74'], rotation=45, wrap=True)
ax.set_xlabel('Age')
ax.set_ylabel('Average BMI')
ax.legend(loc='lower right')
fig.tight_layout()

plt.savefig('line chart/png/17.png')
plt.clf()