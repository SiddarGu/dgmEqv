
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.figure(figsize = (12, 8))
ax = plt.subplot()
ax.plot(["2020", "2021", "2022", "2023", "2024", "2025"], 
        [4500, 5000, 5500, 6000, 6500, 7000], 
        color = 'r', linestyle = '--', marker = 'o', label = 'Domestic Tourism')
ax.plot(["2020", "2021", "2022", "2023", "2024", "2025"], 
        [3000, 3500, 4000, 4500, 5000, 5500], 
        color = 'b', linestyle = '--', marker = 'o', label = 'International Tourism')
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.set_xlabel('Year', fontsize = 12)
ax.set_ylabel('Tourism', fontsize = 12)
ax.legend(fontsize = 12, loc = 'best')
ax.set_title('Increase in Global Tourism from 2020 to 2025', fontsize = 16)
plt.tight_layout()
plt.savefig('line chart/png/235.png')
plt.clf()