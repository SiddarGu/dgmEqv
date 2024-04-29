
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(14, 6))
ax = fig.add_subplot(111)

Year = [2010, 2011, 2012, 2013, 2014, 2015] 
Carbon_Emission = [5000, 4800, 4500, 4200, 4000, 3800] 
Renewable_Energy = [25, 30, 35, 40, 45, 50]
Paper_Recycled = [200, 220, 240, 260, 280, 300]

ax.plot(Year, Carbon_Emission, color='red', marker='o', label="Carbon Emission")
ax.plot(Year, Renewable_Energy, color='blue', marker='o', label="Renewable Energy")
ax.plot(Year, Paper_Recycled, color='green', marker='o', label="Paper Recycled")

ax.set_xticks(Year)
ax.set_title("Carbon Emission, Renewable Energy, and Paper Recycling Trends in the US from 2010 to 2015")
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False, fontsize='medium')
plt.tight_layout()
plt.savefig('line chart/png/479.png')
plt.clf()