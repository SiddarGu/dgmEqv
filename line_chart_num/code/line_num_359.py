
import matplotlib.pyplot as plt 
import numpy as np 

x_data = np.array([2018, 2019, 2020, 2021])
y_data1 = np.array([400, 500, 550, 600])
y_data2 = np.array([200000, 250000, 300000, 350000])
y_data3 = np.array([3000, 4000, 4500, 5000])

fig = plt.figure(figsize=(12, 8))
plt.title('Impact of charity and nonprofit organizations on the society')
plt.xlabel('Year')
plt.ylabel('Value')

plt.xticks(x_data)
plt.grid(True, linestyle='--')

plt.plot(x_data, y_data1, color='red', marker='o', label='Donations (million dollars)')
plt.plot(x_data, y_data2, color='green', marker='^', label='Volunteer Hours')
plt.plot(x_data, y_data3, color='blue', marker='s', label='Number of Volunteers')

for a,b,c in zip(x_data, y_data1, y_data2): 
    plt.text(a, b+c/50, b, ha='center', va= 'bottom',fontsize=10)

plt.legend(loc='best', fontsize=10)
plt.tight_layout()
plt.savefig('line chart/png/144.png')
plt.clf()