
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12,8))
plt.xticks(np.arange(2015,2023,1))

plt.title('Global temperature and CO2 emission trend from 2015 to 2022')
plt.xlabel('Year')
plt.ylabel('Temperature(degrees) / CO2 Emission(kilotonnes)')
plt.grid(linestyle='--')

plt.plot(np.arange(2015,2023,1), [15,14,13,12,12,13,15,18], label='Temperature(degrees)')
plt.plot(np.arange(2015,2023,1), [3600,4000,4200,4400,4600,4800,5000,5200], label='CO2 Emission(kilotonnes)')
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1, fancybox=True, shadow=True)

plt.tight_layout()
plt.savefig('line chart/png/367.png')
plt.clf()