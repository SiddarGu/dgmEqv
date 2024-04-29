

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))

month = ['January','February','March','April','May','June','July','August']
wind_power = [5.8, 6.3, 6.1, 7.2, 7.4, 7.8, 6.7, 8.1]
solar_power = [6.2, 5.8, 7.3, 6.5, 7.8, 6.9, 8.2, 7.3]

plt.plot(month, wind_power, color='blue', marker='o', linestyle='dashed', label='Wind Power (GW)')
plt.plot(month, solar_power, color='red', marker='o', linestyle='dashed', label='Solar Power (GW)')

plt.xticks(month, rotation=45)
plt.xlabel('Month')
plt.title('Renewable energy sources in Australia in 2021')
plt.legend()
plt.tight_layout()
plt.savefig('line chart/png/314.png')
plt.clf()